n, m = list(map(int, input().split()))

p = ('Akshat', 'Malvika')

if min(n, m) % 2 == 0:
    print(p[1])
else:
    print(p[0])
