t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    a = []
    for __ in range(n):
        a.append(list(input()))

    o = 0
    for i in range(n):
        if a[i][-1] == 'R':
            o += 1

    for i in range(m):
        if a[-1][i] == 'D':
            o += 1

    print(o)
