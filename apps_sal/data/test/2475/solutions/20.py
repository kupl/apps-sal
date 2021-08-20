from itertools import accumulate
(N, *S) = map(int, open(0).read().split())
ans = 0
for dx in range(1, N - 1):
    (k, r) = divmod(N - 1, dx)
    if r == 0:
        k = (k + 1) // 2
    ans = max(ans, max(accumulate((a + b for (a, b) in zip(S[:dx * k:dx], S[N - 1:N - 1 - dx * k:-dx])))))
print(ans)
