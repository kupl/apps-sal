n, k, t = map(int, input().split())
if t < k:
    print(t)
else:
    print(k - max(t - n, 0))
