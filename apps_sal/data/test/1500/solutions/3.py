n, k = map(int, input().split())
a = list(map(int, input().split()))
f = True
nn = a[0]
s = 0
nk = -1
i = 0
while i < n:
    if a[i] - nn <= k:
        nk = a[i]
        i += 1
    else:
        if nk != -1:
            nn = nk
            s += 1
            nk = -1
        else:
            f = False
            print(-1)
            break
if f:
    print(s + 1)
