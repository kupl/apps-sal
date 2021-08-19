from bisect import bisect
(N, Q) = list(map(int, input().split()))
ans = (N - 2) * (N - 2)
wx = wy = 0
Ax = []
Ay = []
for _ in range(Q):
    (t, p) = list(map(int, input().split()))
    p = N - p
    if t == 1:
        i = bisect(Ax, (p, 0))
        if i == len(Ax):
            Ax.append((p, wy))
            wx = p
            rev = N - 2 - wy
        else:
            rev = N - 2 - Ax[i][1]
    else:
        i = bisect(Ay, (p, 0))
        if i == len(Ay):
            Ay.append((p, wx))
            wy = p
            rev = N - 2 - wx
        else:
            rev = N - 2 - Ay[i][1]
    ans -= rev
print(ans)
