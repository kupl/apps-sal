import math

N = int(input())
A = list(map(int,input().split()))

A.sort(reverse=True)

comfortPoint = A[0]

for i in range(N-1)[1::]:
    comfortPoint += A[math.ceil(i/2)]

print(comfortPoint)

