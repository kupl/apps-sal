t = int(input())
for k in range(t):
    n, p = map(int, input().split())
    c = 0
    e = 2 * n + p
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if c < e:
                print(i, j)
                c += 1
