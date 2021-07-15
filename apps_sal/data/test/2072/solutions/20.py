def check(f, speed, t):
    inter = (f[0] - speed[0] * t, f[0] + speed[0] * t)
    for i in range(1, len(f)):
        cur = (f[i] - speed[i] * t, f[i] + speed[i] * t)
        if cur[0] > inter[1] or inter[0] > cur[1]:
            return False
        else:
            inter = (max(cur[0], inter[0]), min(cur[1], inter[1]))
    return True


def binsearch(fr, sp):
    inf = 0
    sup = 10 ** 10
    while sup - inf > 10 ** (-6):
        if check(fr, sp, (sup + inf) / 2):
            sup = (sup + inf) / 2
        else:
            inf = (sup + inf) / 2
    return inf if check(fr, sp, inf) else sup



n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))
print(binsearch(x, v))
