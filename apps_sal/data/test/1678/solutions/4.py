r = input
n, t = map(int, r().split())
arr = [int(x) for x in r().split()]
N = -40**14 - 20**14
presum = [0]


def update(Bit, x):
    while(x <= n):
        Bit[x] += 1
        x += (x & -x)


def get(Bit, x):
    res = 0
    while(x > 0):
        res += Bit[x]
        x -= (x & -x)
    return res


for i in arr:
    presum.append(presum[-1] + i)
fakeIndex = [N]
for i in presum:
    fakeIndex.append(i)
    fakeIndex.append(i - t)
fakeIndex.sort()
Indx = {}
for i, j in enumerate(fakeIndex):
    Indx[j] = i
n = len(fakeIndex)
Bit = [0 for i in range(0, n + 1)]
ans = 0
cnt = 0
for i in presum:
    ans += (cnt - get(Bit, Indx[i - t]))
    update(Bit, Indx[i])
    cnt += 1
print(ans)
