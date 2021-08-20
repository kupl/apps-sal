(a, b, c) = list(map(int, input().split()))
res = 0
for i in range(1 + min(2, a, b, c)):
    res = max(res, i + (a - i) // 3 + (b - i) // 3 + (c - i) // 3)
print(res)
