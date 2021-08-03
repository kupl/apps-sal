from math import gcd
N = int(input())
A = list(map(int, input().split()))
num = gcd(A[0], A[1])
for i in range(2, N):
    num = gcd(num, A[i])
print(num)
