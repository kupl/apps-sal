(n, c) = list(map(int, input().split()))
r = [[0 for i in range(c)] for j in range(100000)]
for _ in range(n):
    (s, t, c) = list(map(int, input().split()))
    for j in range(s - 1, t):
        r[j][c - 1] = 1
ans = 0
for i in range(len(r)):
    ans = max(ans, sum(r[i]))
print(ans)
