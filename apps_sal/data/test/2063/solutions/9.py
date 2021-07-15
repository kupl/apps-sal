n, m, w = map(int, input().split(' '))
h = list(map(int, input().split(' ')))

p = [0] * n

def doit(k):
    ts = 0
    td = 0
    for i in range(n):
        if h[i] + ts < k:
            p[i] = k - ts - h[i]
            td += p[i]
        else:
            p[i] = 0
        ts += p[i]
        if (i >= w - 1):
            ts -= p[i - w + 1]
   # print(' '.join(map(str, [k, td])))
    if (td <= m):
        return 1
    else:
        return 0

mir = min(h)
mar = mir + m
while mar > mir:
    mid = (mar + mir + 1) // 2
    if doit(mid):
        mir = mid
    else:
        mar = mid - 1
print(mir)
