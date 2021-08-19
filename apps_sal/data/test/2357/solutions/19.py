from sys import stdin


def rl():
    return [int(w) for w in stdin.readline().split()]


(t,) = rl()
for _ in range(t):
    (n,) = rl()
    a = rl()
    d = {}
    r = -1
    for (i, x) in enumerate(a):
        if x in d and (r < 0 or r > i - d[x] + 1):
            r = i - d[x] + 1
        d[x] = i
    print(r)
