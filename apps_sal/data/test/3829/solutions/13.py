(m, n) = map(int, input().split())
sum = 0.0
for i in range(1, m + 1):
    sum += i * ((1.0 * i / m) ** n - ((i - 1.0) / m) ** n)
print('%.10lf' % sum)
