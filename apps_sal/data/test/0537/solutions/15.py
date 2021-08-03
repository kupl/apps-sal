def read(): return map(int, input().split())


n, k = read()
p = n // 2 // (k + 1)
print(p, p * k, n - p * (k + 1))
