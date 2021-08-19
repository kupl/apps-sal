(a, b, c, k) = map(int, input().split())
result = min(a, k)
k -= a
if k > 0:
    k -= b
if k > 0:
    result -= min(c, k)
print(result)
