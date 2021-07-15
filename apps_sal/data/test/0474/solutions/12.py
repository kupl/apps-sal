N = int(input())
A = [int(a) for a in input().split()]

m = max(A)
ma = 0
c = 0
for i in range(N):
    if A[i] == m:
        c += 1
        ma = max(ma, c)
    else:
        c = 0
print(ma)
