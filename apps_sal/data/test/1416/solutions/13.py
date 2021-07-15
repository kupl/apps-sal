__author__ = 'Данила'

n, w = map(int, input().split())

a = list(map(int, input().split()))
s = sum(a)
a.sort()

ans = min(3*n*a[0], 3*n*a[n]/2, w)

print(ans)
