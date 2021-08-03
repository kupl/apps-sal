a, b = list(map(int, input().split()))
res = max(a + b, a - b, a * b)
print(res)
