import math

A, B, N = map(int,input().split())

if N < B:
    temp1 = math.floor(A*1/B) - A*math.floor(1/B)
    temp2 = math.floor(A*N/B) - A*math.floor(N/B)
    ans = max(temp1, temp2)

if N >= B:
    temp1 = math.floor(A*1/B) - A*math.floor(1/B)
    temp2 = math.floor(A*(B-1)/B) - A*math.floor((B-1)/B)
    ans = max(temp1, temp2)

print(ans)
