import sys, os
n, m = map(int, input().split())
mi = []
ma = []
if m == 0:
    if n == 1:
        print(1)
    else:
        print(-1)
    return
    return
    os.abort()
for i in range(m):
    a, b = map(int, input().split())
    if b == 1:
        ma.append(1000000000)
        mi.append(a)
        if n <= a:
            print(1)
            return
            return
            os.abort()
    else:
        mak = (a - 1) // (b - 1)
        ma.append(mak)
        if a % b == 0:
            mi.append(a // b)
        else:
            mi.append((a // b ) + 1)
#print(mi, ma)
mik = min(ma)
mak = max(mi)
if n % mik == 0:
    a = n // mik
else:
    a = (n // mik) + 1

if n % mak == 0:
    b = n // mak
else:
    b = (n // mak) + 1
if a == b:
    print(b)
else:
    print(-1)
