a, b, k = map(int, input().split())
c = min(a, k)
print(a - c, max(0, b - k + c))
