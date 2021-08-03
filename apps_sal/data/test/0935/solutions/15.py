__author__ = 'Gleb'
a = input().split()
n, m = a
n, m = int(n), int(m)
if m < n:
    n = m
if n % 2 == 0:
    print('Malvika')
else:
    print('Akshat')
