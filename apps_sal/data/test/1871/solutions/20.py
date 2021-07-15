(n, m), a, t, h = list(map(int, input().split())), list(map(int, input().split())), 0, 0

a.sort()

for i in range(n):
    if (m - i) <= 0:
        t = t + a[i] * 1
    else:
        t = t + a[i] * (m - i)

print( t )
