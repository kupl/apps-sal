__author__ = 'Gleb'
n, m, a, b = input().split()
n, m, a, b = int(n), int(m), int(a), int(b)
if a * m < b:
    print(a * n)
else:
    summ = int(n / m) * b
    n = n % m
    if a * n < b:
        print(summ + a * n)
    else:
        print(summ + b)
