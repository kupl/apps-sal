def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


n = int(input())
for eq in range(n):
    (a, b) = map(int, input().split())
    if gcd(a, b) == 1:
        print('Finite')
    else:
        print('Infinite')
