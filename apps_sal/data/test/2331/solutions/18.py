def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


n = int(input())
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if gcd(a, b) == 1:
        print('Finite')
    else:
        print('Infinite')
