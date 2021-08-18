x, y, l, r = list(map(int, input().split()))

unl = []
for i in range(0, 70):
    for j in range(0, 70):
        xx = x**i + y**j
        if (xx >= l and xx <= r):
            unl.append(xx)

unl.sort()

if (len(unl) == 0):
    print(r - l + 1)
    return

diff = []
if (unl[0] != l):
    diff.append(unl[0] - l)

if (unl[-1] != r):
    diff.append(r - unl[-1])

for i in range(1, len(unl)):
    d = (unl[i] - unl[i - 1] - 1)
    if (d > 0):
        diff.append(d)


diff.sort()

if (len(diff) == 0):
    print(0)

else:
    print(diff[-1])
