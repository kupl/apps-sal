k, d, t = list(map(int, input().split()))

if d <= k:
    c = 2 * k + (d - k % d) % d
    r = 2 * t % c
    periodTime = k + (d - k % d) % d
    nrFullPeriods = 2 * t // c
    if r <= 2 * k:
        tailTime = r / 2
    else:
        tailTime = r - k
else:
    c = 2 * k + (d - k)
    r = 2 * t % c
    periodTime = d
    nrFullPeriods = 2 * t // c
    if r <= 2 * k:
        tailTime = r / 2
    else:
        tailTime = r - k
print(nrFullPeriods * periodTime + tailTime)
