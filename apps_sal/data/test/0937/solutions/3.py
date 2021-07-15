n,k = list(map(int,input().split()))

A = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]

the = 0

for i in range(n):
    if T[i]:
        the += A[i]
        A[i] = 0

s = sum(A[:k])
boost = s
for i in range(k,n):
    s = s - A[i-k] + A[i]
    boost = max(s,boost)

print(the+boost)

