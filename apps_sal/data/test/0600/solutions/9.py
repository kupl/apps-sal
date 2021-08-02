a = int(input())
b = int(input())
n = abs(a - b)
k = n - (n // 2)
n = n // 2
res = (n * (n + 1)) // 2 + (k * (k + 1)) // 2
print(res)
