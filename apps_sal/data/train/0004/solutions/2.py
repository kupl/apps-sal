from sys import stdin


def rl():
    return [int(w) for w in stdin.readline().split()]


k, = rl()
for _ in range(k):
    n, = rl()
    p = rl()

    q = [0] * n
    for i, x in enumerate(p):
        q[x - 1] = i

    l = r = q[0]
    m = []
    for k, i in enumerate(q):
        if i < l:
            l = i
        elif i > r:
            r = i
        m.append('1' if r - l == k else '0')
    print(''.join(m))
