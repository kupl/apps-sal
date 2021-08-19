n = int(input())
mex = 1
for num in sorted(map(int, input().split())):
    if num >= mex:
        mex += 1
print(mex)
