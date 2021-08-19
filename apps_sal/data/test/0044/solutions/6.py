(d, k, a, b, t) = map(int, input().split(' '))
cyc = (d + k - 1) // k
alldrive = d * a + t * (cyc - 1)
allwalk = d * b
minn = min(alldrive, allwalk)
if (d + k - 1) // k <= 10:
    for x in range(1, (d + k - 1) // k):
        time = x * k * a + (x - 1) * t + b * (d - x * k)
        minn = min(minn, time)
else:
    for x in [1, (d + k - 1) // k - 1]:
        time = x * k * a + (x - 1) * t + b * (d - x * k)
        minn = min(minn, time)
print(minn)
