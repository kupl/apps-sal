from math import *
# n,k=map(int,input().split())
#A = list(map(int,input().split()))
n = int(input())
A = list(map(int, input().split()))
ans = -1
maxs = 0
for j in range(n):
    if(A[j] > maxs):
        ans = j + 1
        break
    else:
        maxs = max(maxs, A[j] + 1)
print(ans)
