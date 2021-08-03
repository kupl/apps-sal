k, d, t = list(map(int, input().split()))

if (k % d == 0):
    d = (int(k / d)) * d
else:
    d = (int(k / d) + 1) * d
p = k + (d - k) / 2
z = int(t / p) * d
e = int(t / p) * p
if (t - e < k):
    z += (t - e)
else:
    z += k + (t - e - k) * 2
print(z)
