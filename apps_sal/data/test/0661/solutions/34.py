m, k = map(int, input().split())
x = [*range(1 << m)]
print(*x[::-1] + x if k < 1else x[:k:-1] + x[k - 1::-1] + [k] + x[:k] + x[k + 1:] + [k]if(k < 2**m) & (m > 1)else[-1])
