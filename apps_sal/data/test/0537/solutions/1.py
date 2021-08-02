n, k = list(map(int, input().split()))
s = n // 2
a = s // (k + 1)
b = a * k
c = n - a - b
print(a, b, c)
