from math import gcd
N, X = map(int, input().split())
x = list(map(int, input().split()))

xx = list()
for i in range(N):
    xx.append(abs(X - x[i]))
num = xx[0]
for i in range(1, N):
    num = gcd(num, xx[i])
print(num)
