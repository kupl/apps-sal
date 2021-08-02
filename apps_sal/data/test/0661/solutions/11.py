m, k = map(int, input().split())
x = [*range(1 << m)]
print(*k < 1 and x + x[::-1] or k < 1 << m > 2 and [k] + x[k + 1:] + x[:k] + [k] + x[k - 1::-1] + x[:k:-1] or [-1])
