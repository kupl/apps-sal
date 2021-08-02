n = int(input())
a = list(map(int, input().split()))
a.sort()

mex = 1
miss = False

i = 0
while i < n:
    while i < n and a[i] < mex:
        i += 1

    if i != n:
        mex += 1

    i += 1

print(mex)
