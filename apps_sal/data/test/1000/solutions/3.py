n, v = map(int, input().split())

result = v - 1 + (n - v) * (n - v + 1) // 2 if n - 1 > v else n - 1
print(result)
