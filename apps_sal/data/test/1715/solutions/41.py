import bisect

a, b, q = map(int, input().split())
s = []
t = []
for i in range(a):
    s.append(int(input()))
for i in range(b):
    t.append(int(input()))
for _ in range(q):
    x = int(input())

    ans = [0, 0, 0]

    i = bisect.bisect_left(s, x)
    if i == 0:
        sl = 100000000000
    else:
        sl = abs(s[i - 1] - x)
    if i == a:
        sr = 100000000000
    else:
        sr = abs(s[i] - x)
    i = bisect.bisect_left(t, x)
    if i == 0:
        tl = 100000000000
    else:
        tl = abs(t[i - 1] - x)
    if i == b:
        tr = 100000000000
    else:
        tr = abs(t[i] - x)
    ans[0] = max(tl, sl)
    ans[1] = max(tr, sr)
    ans[2] = min(2 * tl + sr, 2 * sl + tr, 2 * sr + tl, 2 * tr + sl)
    print(min(ans))
