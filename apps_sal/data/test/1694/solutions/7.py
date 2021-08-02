n, m, s, f = list(map(int, input().split()))

ans, p = '', 1
if s < f:
    for i in range(m):
        t, l, r = list(map(int, input().split()))
        if t > p:
            if t - p < f - s:
                ans += 'R' * (t - p)
                s += t - p
            else:
                ans += 'R' * (f - s)
                s = f
                break
        p = t + 1
        if s + 1 < l or s > r:
            ans += 'R'
            s += 1
            if s == f:
                break
        else:
            ans += 'X'
else:
    for i in range(m):
        t, l, r = list(map(int, input().split()))
        if t > p:
            if t - p < s - f:
                ans += 'L' * (t - p)
                s -= t - p
            else:
                ans += 'L' * (s - f)
                s = f
                break
        p = t + 1
        if s < l or s - 1 > r:
            ans += 'L'
            s -= 1
            if s == f:
                break
        else:
            ans += 'X'
print(ans + ('R' * (f - s) if f > s else 'L' * (s - f)))
