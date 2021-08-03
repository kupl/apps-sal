import bisect

A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]

st = [0] * A
ts = [0] * B

for i in range(A):
    tmp = bisect.bisect_left(t, s[i])
    if tmp == 0:
        st[i] = t[0] - s[i]
    elif tmp == B:
        st[i] = s[i] - t[-1]
    else:
        st[i] = min(s[i] - t[tmp - 1], t[tmp] - s[i])

for i in range(B):
    tmp = bisect.bisect_left(s, t[i])
    if tmp == 0:
        ts[i] = s[0] - t[i]
    elif tmp == A:
        ts[i] = t[i] - s[-1]
    else:
        ts[i] = min(t[i] - s[tmp - 1], s[tmp] - t[i])

for i in range(Q):
    cand = set()
    tmp = bisect.bisect_left(s, x[i])
    if tmp > 0:
        cand.add(x[i] - s[tmp - 1] + st[tmp - 1])
    if tmp < A:
        cand.add(s[tmp] - x[i] + st[tmp])

    tmp = bisect.bisect_left(t, x[i])
    if tmp > 0:
        cand.add(x[i] - t[tmp - 1] + ts[tmp - 1])
    if tmp < B:
        cand.add(t[tmp] - x[i] + ts[tmp])

    print(min(cand))
