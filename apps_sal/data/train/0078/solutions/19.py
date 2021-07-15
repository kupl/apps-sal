q = int(input())
for i in range(q):
    n,m = list(map(int,input().split()))
    a = [input() for _ in range(n)]
    a_t = list(zip(*a))
    mx_1 = mx_2 = 0
    idx_1 = []
    idx_2 = []
    for j,i in enumerate(a):
        temp = i.count('*')
        if temp > mx_1:
            mx_1 = temp
            idx_1 = [j]
        elif temp == mx_1:
            idx_1.append(j)
    for j,i in enumerate(a_t):
        temp = i.count('*')
        if temp > mx_2:
            mx_2 = temp
            idx_2 = [j]
        elif temp == mx_2:
            idx_2.append(j)
    ans = 0
    for i in idx_1:
        for j in idx_2:
            if a[i][j] == '.':
                ans = -1
    print(n+m-mx_1-mx_2+ans)


