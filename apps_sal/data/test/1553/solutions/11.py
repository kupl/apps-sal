N, H = list(map(int, input().split()))
A = list(map(int, input().split()))


def isok(k):
    if k == 0:
        return True
    sa = list(sorted(A[:k], reverse=True))
    h = 0
    for a in sa[::2]:
        h += a
        if h > H:
            return False
    return True


ok = 0
ng = N + 1
while ng - ok > 1:
    m = (ok + ng) // 2
    if isok(m):
        ok = m
    else:
        ng = m
print(ok)
