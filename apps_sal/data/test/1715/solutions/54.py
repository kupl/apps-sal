import bisect
a, b, q = map(int, input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
x = [int(input()) for _ in range(q)]
for r in x:
    k = bisect.bisect(s, r)
    l = bisect.bisect(t, r)
    ans = 10 ** 11
    if k < a and l < b:
        ans = min(ans, max(s[k], t[l]) - r)
    if k > 0 and l > 0:
        ans = min(ans, r - min(s[k-1], t[l-1]))
    if k < a and l > 0:
        ans = min(ans, s[k] + r - t[l-1] * 2, s[k] * 2 - r - t[l-1])
    if k > 0 and l < b:
        ans = min(ans, t[l] + r - s[k-1] * 2, t[l] * 2 - r - s[k-1])
    print(ans)
