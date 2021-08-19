M = 998244353
(N, S) = list(map(int, input().split()))
ans = 0
prev = [0] * S
for (i, a) in enumerate(map(int, input().split()), 1):
    if a > S:
        continue
    prev[0] = i
    ans = (ans + prev[S - a] * (N - i + 1)) % M
    for (j, s) in enumerate(prev[:S - a], a):
        prev[j] += s
print(ans)
