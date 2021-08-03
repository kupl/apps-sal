k, n, w = map(int, input().split())
s = n - k * w * (w + 1) // 2
#print(s, k, n, w)
if s < 0:
    print(-s)
else:
    print(0)
