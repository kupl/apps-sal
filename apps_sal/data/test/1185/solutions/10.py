n, m, k = map(int, input().split())

p = list(map(int, input().split()))

if m == 1:
    p.sort()
    print(sum(p[n - k:n]))
else:
    curr_s2 = [0] + p
    for i in range(1, n + 1):
        curr_s2[i] += curr_s2[i - 1]

    d = [[0 for i in range(n + 1)] for j in range(k + 1)]

    for i in range(1, k + 1):
        for j in range(i * m, n + 1):
            d[i][j] = max(d[i][j - 1], d[i - 1][j - m] + curr_s2[j] - curr_s2[j - m])

    print(d[k][n])
