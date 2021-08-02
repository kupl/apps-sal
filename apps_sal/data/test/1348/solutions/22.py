import sys
input = sys.stdin.readline
I = lambda: list(map(int, input().split()))

n, k = I()
d = I(); ed = []
d = sorted([[d[i], i + 1] for i in range(n)])
i = 1; cur = [d[0][1]]; l = 0; f = 1
if d[0][0] != 0:
    f = 0
while i < n:
    x = len(cur); m = x * (k - 1) if i != 1 else k
    r = 0; j = 0; ll = []
    while i < n and d[i][0] == l + 1:
        if j >= x:
            r = m + 1; break
        ed.append([cur[j], d[i][1]])
        ll.append(d[i][1])
        i += 1; r += 1
        if r == ((j + 1) * (k - 1) if l != 0 else k):
            j += 1
    if r == 0 or r > m:
        f = 0; break
    cur = list(ll)
    l += 1
if f:
    print(len(ed))
    for i in range(len(ed)):
        print(*ed[i])
else:
    print(-1)
