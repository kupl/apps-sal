def R(): return map(int, input().split())


k, d, t = R()
p = (k // d + (1 if k % d else 0)) * d
kp = k / t
wp = (p - k) / (2 * t)
ri = 1 // (kp + wp) * p
rm = 1 % (kp + wp)
rr = rm / kp * k if rm < kp else k + (rm - kp) / wp * (p - k)
print(ri + rr)
