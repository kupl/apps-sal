N, K = map(int, input().split())
table = [0] * (2 * N + 1)

for i in range(N):
    table[N + i] = table[N - i] = N - i
ans = 0

for i in range(2 * N + 1):
    if  0 <= (j := (K - (i - N) + N)) < 2 * N + 1:
        ans += table[i] * table[j]
print(ans)
