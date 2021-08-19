t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    m = input()
    flag = False
    l = []
    prev = 0
    flag = False
    for i in range(len(m)):
        if flag:
            if m[i] == '0':
                l.append((prev, i - 1))
                flag = False
            else:
                continue
        else:
            if m[i] == '0':
                continue
            else:
                flag = True
                prev = i
    if flag:
        l.append((prev, len(m) - 1))
    # print(l)
    if(len(l) == 1):
        print(a)
    elif (len(l) == 0):
        print(0)
    else:
        ans = a
        for i in range(1, len(l)):
            if (l[i][0] - l[i - 1][1] - 1) * b <= a:
                ans += (l[i][0] - l[i - 1][1] - 1) * b
            else:
                ans += a
        print(ans)
