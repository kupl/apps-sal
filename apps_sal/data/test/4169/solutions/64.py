(n, m) = map(int, input().split(' '))
a = sorted((list(map(int, input().split(' '))) for i in range(n)))
total = 0
for (i, j) in a:
    if j < m:
        m -= j
        total += i * j
    else:
        total += i * m
        break
print(total)
