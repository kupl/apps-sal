a, b = list(map(int, input().split()))
c = b - a - 1
res = c * (c + 1) // 2 - a
print(res)

