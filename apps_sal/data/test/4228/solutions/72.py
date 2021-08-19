(n, a) = map(int, input().split())
x = [a + i - 1 + 1 for i in range(n)]
y = sorted(x, key=lambda i: abs(i))
del y[0]
print(sum(y))
