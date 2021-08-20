from sys import stdin, stdout
(s, x1, x2) = map(int, stdin.readline().split())
(spt, spp) = map(int, stdin.readline().split())
(p, label) = map(int, stdin.readline().split())
vt = 1 / spt
vp = 1 / spp
ans = abs(x2 - x1) * spp
if vt > vp:
    if label == 1:
        if x2 >= x1:
            if p <= x1:
                t = (x1 - p) / (vt - vp)
                ans = min(ans, t + max(x2 - (x1 + t * vp), 0) * spt)
            else:
                t = (s - p + s) / vt
                t += (x1 + t * vp) / (vt - vp)
                x1 += t * vp
                ans = min(ans, t + max(x2 - x1, 0) * spt)
        else:
            t = (s - p) / vt
            t += (s - (x1 - t * vp)) / (vt - vp)
            x1 -= t * vp
            ans = min(ans, t + max(x1 - x2, 0) * spt)
    elif x2 <= x1:
        if p >= x1:
            t = (p - x1) / (vt - vp)
            ans = min(ans, t + max(x1 - t * vp - x2, 0) * spt)
        else:
            t = (p + s) * spt
            t += (s - (x1 - t * vp)) / (vt - vp)
            ans = min(ans, t + max(x1 - t * vp - x2, 0) * spt)
    else:
        t = p * spt
        t += (x1 + t * vp) / (vt - vp)
        x1 += t * vp
        ans = min(ans, t + max(x2 - x1, 0) * spt)
stdout.write(str(int(ans)))
