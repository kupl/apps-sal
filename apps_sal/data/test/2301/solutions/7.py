n = int(input())
A = [int(x) for x in input().split()]
A.sort()
R = [None]*n

R[1::2] = A[:n//2]
R[0::2] = A[n//2:]
r = 0
for i in range(1,n-1):
    r += R[i-1] > R[i] < R[i+1];
print(r)
print(*R)

