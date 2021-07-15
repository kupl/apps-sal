# Fast IO (be careful about bytestring)

# import os,io
# input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

for _ in range(int(input())):
    n,x,y = list(map(int,input().split()))
    minMax = 100000
    minD = 0
    minStart = 0
    for d in range(1,y - x + 1):
        if (y - x) % d != 0 or d * (n-1) < y - x:
            continue
        minElem = x % d
        if minElem == 0:
            minElem = d
        maxElem = minElem + d * (n-1)
        if maxElem < y:
            maxElem = y
            minElem = maxElem - d * (n-1)
        if maxElem < minMax:
            minMax = maxElem
            minStart = minElem
            minD = d
    ans = []
    elem = minStart
    for i in range(n):
        ans.append(str(elem))
        elem += minD
    print(" ".join(ans))

