n, z, w = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    print(abs(w - a[0]))
else:
    ans = 0
    ans = max(ans, abs(a[-1] - w))
    ans = max(ans, abs(a[-1] - a[-2]))
    print(ans)
