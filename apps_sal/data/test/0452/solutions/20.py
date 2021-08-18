def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)


p, q = list(map(int, input().split()))
N = int(input())
A = list(map(int, input().split()))
znam = 1
chisl = A[N - 1]

for i in range(N - 1, 0, -1):
    chisl, znam = znam, chisl
    chisl += znam * A[i - 1]
if(p * znam == q * chisl):
    print('YES')
else:
    print('NO')
