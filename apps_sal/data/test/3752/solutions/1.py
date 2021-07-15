3

k, d, t = (float(s) for s in input().split())

n = k // d
r = d - k % d
T = n * d
if k % d != 0:
    T += d
dt = k
if k % d != 0:
    dt += r / 2

cnt = t // dt
rem = t % dt
rest = 0
if rem < k:
 rest = rem
else:
 rest = k + (rem - k) * 2

print(cnt * T + rest)

