(n, m) = map(int, input().split())
INF = 10 ** 10
B = [INF] * (1 << n)
B[0] = 0
for _ in range(m):
    (a, b) = map(int, input().split())
    C = list(map(int, input().split()))
    opens = 0
    for c in C:
        opens |= 1 << c - 1
    for i in range(2 ** n):
        if B[i | opens] > B[i] + a:
            B[i | opens] = B[i] + a
if B[(1 << n) - 1] == INF:
    print(-1)
else:
    print(B[(1 << n) - 1])
