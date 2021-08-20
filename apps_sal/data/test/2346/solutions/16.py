def bs(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return 1
        elif arr[mid] > x:
            return bs(arr, l, mid - 1, x)
        else:
            return bs(arr, mid + 1, r, x)
    else:
        return 0


n = int(input())
nrp = []
rc = []
for i in range(n):
    (p, c) = map(int, input().split())
    if c:
        nrp.append(i + 1)
    if not c:
        rc.append(p)
s = []
rc.sort()
for i in nrp:
    if not bs(rc, 0, len(rc) - 1, i):
        s.append(i)
if not s:
    print('-1')
else:
    print(*sorted(s))
