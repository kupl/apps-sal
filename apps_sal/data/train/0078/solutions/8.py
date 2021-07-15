q = int(input())
for _ in range(q):
    n, m = list(map(int, input().split()))
    d = [list(input()) for _ in range(n)]
    count_x = list([x.count('*') for x in d])
    count_y = list([x.count('*') for x in zip(*d)])
    #dt = map(list, zip(*d))
    rls = n+m-1
    for i in range(n):
        for j in range(m):
            a = count_x[i]
            b = count_y[j]
            if d[i][j] == '*':
                rls = min(rls, n+m-a-b)
            else:
                rls = min(rls, n+m-a-b-1)
    print(rls)

