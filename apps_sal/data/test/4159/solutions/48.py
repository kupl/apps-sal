a, b, k = map(int, input().split())
n = min(a, k)
k -= n
print(a - n, max(0, b - k))
