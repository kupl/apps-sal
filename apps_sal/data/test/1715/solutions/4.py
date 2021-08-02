from bisect import bisect_left, bisect_right
A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
for _ in range(Q):
    x = int(input())
    a = bisect_right(s, x)
    b = bisect_right(t, x)
    la = x - s[a - 1] if a > 0 else None
    ra = s[a] - x if a < A else None
    lb = x - t[b - 1] if b > 0 else None
    rb = t[b] - x if b < B else None
    ans = float("inf")
    if la and lb:
        ans = min(ans, max(la, lb))
    if la and rb:
        ans = min(ans, la + 2 * rb, 2 * la + rb)
    if ra and lb:
        ans = min(ans, ra + 2 * lb, 2 * ra + lb)
    if ra and rb:
        ans = min(ans, max(ra, rb))
    print(ans)
