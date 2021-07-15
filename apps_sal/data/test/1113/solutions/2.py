n = int(input())
a = list(map(int, input().split()))

mex = -1
for i in range(n):
    if a[i] <= mex:
        continue
    elif a[i] == mex + 1:
        mex += 1
    else:
        print(i+1)
        return
print(-1)
