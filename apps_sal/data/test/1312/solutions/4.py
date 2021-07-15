n, m = input().split()

n = int(n)
m = int(m)

t = n % m

if t == 0:
    for i in range(m): print(n // m, end = ' ')
else:
    for i in range(m - t): print(n // m, end = ' ')
    for i in range(t): print(n // m + 1, end = ' ')

