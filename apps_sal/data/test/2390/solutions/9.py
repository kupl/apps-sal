from itertools import accumulate

n, c = list(map(int, input().split()))
xs, vs = [], []
for _ in range(n):
    x, v = list(map(int, input().split()))
    xs.append(x)
    vs.append(v)
xs = [0] + xs + [c]
vs = [0] + vs + [0]


def maxcalrrl(xs=xs, vs=vs):
    avsr = list(accumulate(reversed(vs)))[::-1]

    calr = [a - 2 * x for x, a in zip(xs, accumulate(vs))]
    call = [a - (c - x) for x, a in zip(xs, avsr)]

    maxcalr = list(accumulate(calr, max))

    return max([
        call[i + 1] + maxcalr[i] for i in range(n + 1)
    ])


def maxcalrll(xs=xs, vs=vs):
    xsr = [c - x for x in xs][::-1]
    vsr = vs[::-1]
    return maxcalrrl(xsr, vsr)


answer = max([maxcalrrl(), maxcalrll()])
print(answer)
