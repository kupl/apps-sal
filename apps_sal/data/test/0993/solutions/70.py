from collections import Counter
(N, M) = list(map(int, input().split()))
(*A,) = list(map(int, input().split()))
ac = [0] * (N + 1)
for i in range(1, N + 1):
    ac[i] = (ac[i - 1] + A[i - 1]) % M
c = Counter(ac)
ans = 0
for i in list(c.values()):
    ans += i * (i - 1) // 2
print(ans)
