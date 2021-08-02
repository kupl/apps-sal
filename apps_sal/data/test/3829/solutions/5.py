m, n = list(map(int, input().split()))
f = lambda x: (x / m) ** n
print("{:.9}".format(sum((f(i + 1) - f(i)) * (i + 1) for i in range(m))))
