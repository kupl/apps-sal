n, p, t = input().split()
n = int(n)
t = int(t)
p = float(p)
ans = 0.0
s = t
if abs(1.0 - p) > 1e-6:
    a1 = 1.0
    for i in range(1, t + 1):
        a1 = a1 * (t - i + 1) / i if i <= t else 0
        a1 = a1 * p
        while (a1 > 1e5) and (s > i):
            a1 *= (1 - p)
            s -= 1
        while (s < i):
            a1 /= (1 - p)
            s += 1
        a2 = (1 - p) ** (s - i)
        #print(a1, a2, s, i)
        ans += a1 * a2 * min(i, n)
else:
    ans = min(n, t)
print(ans)
