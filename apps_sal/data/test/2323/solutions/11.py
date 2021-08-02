import math


def f5(seq, idfun=None):
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result


def upper_bound(v, val):
    l = 0
    r = len(v)
    while l + 1 < r:
        mid = (l + r) // 2
        if v[mid] <= val:
            l = mid
        else:
            r = mid
    return r


N = list(map(int, input().split()))
inp = [*list(map(int, input().split()))]
inp = sorted(f5(inp))
N = len(inp)
mp = {}
v = []
i = 0
while i < N - 1:
    gap = inp[i + 1] - inp[i]
    v.append(gap)
    mp[gap] = 0
    i = i + 1
for gap in v:
    mp[gap] = mp[gap] + 1
v.append(0)
v = sorted(f5(v))
psum1 = [0] * (len(mp) + 1)
psum0 = [0] * (len(mp) + 1)

i = 1
while i <= len(mp):
    cur = v[i]
    psum1[i] = psum1[i - 1] + (psum0[i - 1] * (cur - v[i - 1])) + mp[cur]
    psum0[i] = psum0[i - 1] + mp[cur]
    i = i + 1
Q = int(input())
ansstring = ''
while Q > 0:
    l, r = list(map(int, input().split()))
    siz = r - l
    idx = upper_bound(v, siz) - 1
    ans = N * (siz + 1)
    remain = siz - v[idx]
    ans -= psum1[idx]
    ans -= psum0[idx] * remain
    ansstring += str(ans) + ' '
    Q = Q - 1
print(ansstring)
