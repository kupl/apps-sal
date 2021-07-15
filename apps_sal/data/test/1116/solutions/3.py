def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

N = int(input())
for _ in range(N):
    a, b, k = list(map(int, input().split()))
    g = gcd(a, b)
    mi = min(a, b)
    ma = max(a, b)
    A = ma//g - 1
    B = mi//g
    
    if B * (k-1) < A:
        print("REBEL")
    else:
        print("OBEY")

