k, n, w = map(int, input().split())

s = w * (k + w * k) // 2
r = max(s - n, 0)
print(r)
