(n, a, b, c, d) = list(map(int, input().split()))
l = max(1 - b + c, 1 - a + d, 1 - a - b + c + d)
h = min(n - b + c, n - a + d, n - a - b + c + d)
if l < 0:
    l = 1
if h > n:
    h = n
if h < l:
    print(0)
else:
    print(n * (h - l + 1))
