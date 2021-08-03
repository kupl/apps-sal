m, k = map(int, input().split())
x = [*range(1 << m)]
print(*(x + x[::-1]) * (k < 1) or ([k] + x[k + 1:] + x[:k] + [k] + x[k - 1::-1] + x[:k:-1]) * (k < 1 << m > 2) or [-1])
