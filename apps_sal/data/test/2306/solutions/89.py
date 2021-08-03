N = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))

maxv = [0] + [min(v[i], v[i + 1]) for i in range(N - 1)] + [0]
for i in reversed(range(N)):
    if maxv[i] - maxv[i + 1] > t[i]:
        maxv[i] = maxv[i + 1] + t[i]
for i in range(N):
    if maxv[i + 1] - maxv[i] > t[i]:
        maxv[i + 1] = maxv[i] + t[i]


def kyori(start, stop, mxv, ti):
    if stop >= start:
        if stop - start >= ti:
            return (stop + start) * ti / 2
        elif mxv <= stop:
            return ti * mxv - (mxv - start)**2 / 2
        else:
            x = (stop - start + ti) / 2
            if mxv >= start + x:
                return (start + start + x) * x / 2 + (stop + stop + ti - x) * (ti - x) / 2
            else:
                return ti * mxv - ((mxv - start)**2 + (mxv - stop)**2) / 2
    else:
        x = (stop - start + ti) / 2
        if mxv >= start + x:
            return (start + start + x) * x / 2 + (stop + stop + ti - x) * (ti - x) / 2
        else:
            return ti * mxv - ((mxv - start)**2 + (mxv - stop)**2) / 2


ans = 0
for i in range(N):
    ans += kyori(maxv[i], maxv[i + 1], v[i], t[i])

print(ans)
