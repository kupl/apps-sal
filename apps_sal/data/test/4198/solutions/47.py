from math import log10, floor

a, b, x = map(int, input().split())

n, m = 0, 0
for i in range(10):
    if a*10**i+b*(i+1) <= x:
        n = 10**i
        m = i+1

if n == 0:
    print(0)
else:
    print(min(10**9, 10*n-1, n+(x-a*n-b*m)//a))
