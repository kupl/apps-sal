d, k, a, b, t = [int(x) for x in input().split()]
if (d <= k):
    print(a * d)
    return
fir = a * k + t - k * b
sec = d * b - k * b + a * k
maxc = d // k - 1
for x in range(maxc - 10, maxc + 10):
    if (k * (x + 1) <= d):
        maxc = x
c = maxc
print(min(c * t + c * a * k + k * a + t + a * (d - c * k - k), min(sec, maxc * fir + sec)))
