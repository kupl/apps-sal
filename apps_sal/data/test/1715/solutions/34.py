from bisect import bisect_left
(a, b, q) = list(map(int, input().split()))
dummy = 10 ** 18 + 1
s = [-dummy] + [int(input()) for _ in range(a)] + [dummy]
t = [-dummy] + [int(input()) for _ in range(b)] + [dummy]
x = [int(input()) for _ in range(q)]
for i in x:
    (idx_s, idx_t) = (bisect_left(s, i), bisect_left(t, i))
    ans = dummy
    for j in [s[idx_s - 1], s[idx_s]]:
        for k in [t[idx_t - 1], t[idx_t]]:
            (res1, res2) = (abs(j - i) + abs(k - j), abs(k - i) + abs(j - k))
            ans = min(ans, res1, res2)
    print(ans)
