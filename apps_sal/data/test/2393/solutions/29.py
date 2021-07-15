t = int(input())
for i in range(0, t):
    s = input()
    bal = 0
    a = []
    n = len(s)
    for j in range(0, n):
        if s[j] == 'o':
            bal = 1
        elif bal == 1 and s[j] == 'n':
            bal += 1
        elif bal == 2 and s[j] == 'e':
            bal = 0
            a.append([j - 2, j, 1])
        else:
            bal = 0
    bal = 0
    for j in range(0, n):
        if s[j] == 't':
            bal = 1
        elif bal == 1 and s[j] == 'w':
            bal += 1
        elif bal == 2 and s[j] == 'o':
            bal = 0
            a.append([j - 2, j, 2])
        else:
            bal = 0
    a.sort()
    ans = []
    length = len(a)
    if length == 0:
        print(0)
        print("")
    else:
        if a[0][2] == 1:
            if not (a[0][0] - 1 >= 0 and s[a[0][0] - 1] == 'o'):
                ans.append(a[0][0] + 1)
            else:
                ans.append(a[0][0] + 2)
        else:
            if not (a[0][1] + 1 < n and s[a[0][1] + 1] == 'o'):
                ans.append(a[0][1] + 1)
            else:
                ans.append(a[0][1])
        for j in range(1, length):
            if a[j][2] == 1:
                if a[j][0] != a[j - 1][1]:
                    if not (a[j][0] - 1 >= 0 and s[a[j][0] - 1] == 'o'):
                        ans.append(a[j][0] + 1)
                    else:
                        ans.append(a[j][0] + 2)
            else:
                if not (a[j][1] + 1 < n and s[a[j][1] + 1] == 'o'):
                    ans.append(a[j][1] + 1)
                else:
                    ans.append(a[j][1])
        print(len(ans))
        print(*ans)

