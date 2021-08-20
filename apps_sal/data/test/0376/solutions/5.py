import sys
n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
s = [[] for g in d]
mxpt = [-2000000000.0, -2000000000.0]
mxcnt = [0, 0]
for i in d:
    if i > mxpt[0]:
        mxpt[1] = mxpt[0]
        mxcnt[1] = mxcnt[0]
        mxpt[0] = i
        mxcnt[0] = 1
    elif i == mxpt[0]:
        mxcnt[0] += 1
    elif i > mxpt[1]:
        mxpt[1] = i
        mxcnt[1] = 1
    else:
        mxcnt[1] += i == mxpt[1]
for i in range(1, n):
    (a, b) = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    s[a] += [b]
    s[b] += [a]
mx = int(2000000000.0)
for i in range(n):
    nmx = [] + mxcnt
    tmpmax = d[i]
    for k in s[i]:
        if d[k] == mxpt[0]:
            nmx[0] -= 1
        elif d[k] == mxpt[1]:
            nmx[1] -= 1
    if nmx[0] != mxcnt[0]:
        tmpmax = mxpt[0] + 1
    elif nmx[1] != mxcnt[1]:
        tmpmax = max(tmpmax, mxpt[1] + 1)
    if d[i] == mxpt[0]:
        nmx[0] -= 1
    elif d[i] == mxpt[1]:
        nmx[1] -= 1
    if nmx[0]:
        tmpmax = mxpt[0] + 2
    elif nmx[1]:
        tmpmax = max(mxpt[1] + 2, tmpmax)
    mx = min(mx, tmpmax)
print(mx)
