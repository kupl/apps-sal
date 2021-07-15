from math import gcd

N, M = map(int, input().split())
A = list(map(int, input().split()))

f = lambda n: 0 if n%2 else f(n>>1)+1
x = f(A[0])

if sum(x!=f(a) for a in A):
    print(0)
    return

A = [a>>x for a in A]

y = 1
for a in A:
    y = y*a//gcd(y, a)
    if y<<(x-1) > M:
        print(0)
        return

print((M//(y<<(x-1))+1)//2)
