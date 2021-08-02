n = int(input())
L = sorted([int(i) for i in input().split()])

i = 0
mex = 1
while i < n:
    if mex <= L[i]:
        mex += 1
    i += 1
print(mex)
