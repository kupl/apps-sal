__author__ = 'Daniil'
n, t = list(map(int, input().split()))

a = list(map(int, input().split()))
i = 0
while i != t - 1:
    i += a[i]
    if i > t - 1:
        print('NO')
        quit()
print('YES')
