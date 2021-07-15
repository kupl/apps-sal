n, m = map(int, input().split())
A = [0]*m

for i in range(n):
    B = list(input())
    for j in range(m):
        if B[j]=='*':
            A[j]+=1
mp = 0
ms = 0
for i in range(m-1):
    if A[i]<A[i+1] and A[i+1]-A[i]>mp:
        mp = A[i+1]-A[i]
    elif A[i]>A[i+1] and A[i]-A[i+1]>ms:
        ms = A[i]-A[i+1]
print(mp, ms)
