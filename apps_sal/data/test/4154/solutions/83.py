from itertools import accumulate
(N, M) = list(map(int, input().split()))
imos = [0] * (N + 2)
for i in range(M):
    (l, r) = list(map(int, input().split()))
    imos[l] += 1
    imos[r + 1] -= 1
imos = list(accumulate(imos))
ans = 0
for im in imos:
    ans += im == M
print(ans)
