RMAX = 1000
p, q, l, r = list(map(int, input().split()))


def rl():
    a, b = list(map(int, input().split()))
    return a, b


x = [rl() for _ in range(p)]
xline = [False] * (RMAX + 1)
for a, b in x:
    for i in range(a, b + 1):
        xline[i] = True
y = [rl() for _ in range(q)]


def test(t):
    for a, b in y:
        for i in range(t + a, t + b + 1):
            if i > RMAX:
                break
            if xline[i] == True:
                return 1
    return 0


ans = sum(test(t) for t in range(l, r + 1))
print(ans)
