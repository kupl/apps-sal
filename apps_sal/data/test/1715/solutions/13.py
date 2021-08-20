from bisect import bisect_right
(a, b, q) = map(int, input().split())
s = [-float('inf')] + [int(input()) for i in range(a)] + [float('inf')]
t = [-float('inf')] + [int(input()) for i in range(b)] + [float('inf')]
x = [int(input()) for i in range(q)]
for i in range(q):
    X = x[i]
    (l, r) = (bisect_right(s, X), bisect_right(t, X))
    ans = float('inf')
    ans = min(ans, abs(s[l - 1] - X) + abs(t[r - 1] - s[l - 1]), abs(t[r - 1] - X) + abs(s[l - 1] - t[r - 1]))
    ans = min(ans, abs(s[l - 1] - X) + abs(t[r] - s[l - 1]), abs(t[r] - X) + abs(s[l - 1] - t[r]))
    ans = min(ans, abs(s[l] - X) + abs(t[r - 1] - s[l]), abs(t[r - 1] - X) + abs(s[l] - t[r - 1]))
    ans = min(ans, abs(s[l] - X) + abs(t[r] - s[l]), abs(t[r] - X) + abs(s[l] - t[r]))
    print(ans)
