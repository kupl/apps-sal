import math
N = int(input())
lsA = list(map(int, input().split()))
gcd = lsA[0]
for i in range(1, N):
    gcd = math.gcd(gcd, lsA[i])
print(gcd)
