3


def readln(): return tuple(map(int, input().split()))


n, = readln()
a = readln()
m = min(a)
ind = [i for i, _ in enumerate(a) if _ == m][-1]
cnt = [0] * 11
cnt[ind + 1] = n // m
ost = n % m
while cnt[ind + 1] > 0:
    ost += m
    var = [i for i, _ in enumerate(a) if m < _ <= ost and i > ind]
    if var:
        cnt[ind + 1] -= 1
        cnt[var[-1] + 1] += 1
        ost -= a[var[-1]]
    else:
        break
if cnt[ind + 1]:
    for i in range(9, 0, -1):
        print(str(i) * cnt[i], end='')
    print()
else:
    print(-1)
