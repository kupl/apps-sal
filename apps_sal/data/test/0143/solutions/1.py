n = int(input())
A = [int(x) for x in input().split()]
A.sort()
mex = 1
for i in range(n):
    if A[i] >= mex:
        A[i] = mex
        mex += 1
print(mex)
