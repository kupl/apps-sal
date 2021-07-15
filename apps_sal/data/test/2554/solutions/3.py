from sys import exit,stdin,stderr
def rl():
    return [int(w) for w in stdin.readline().split()]

def maxsum(b):
    cur = r = 0
    for x in b:
        cur += x
        if cur < 0:
            cur = 0
        elif cur > r:
            r = cur
    return r

T, = rl()
for _ in range(T):
    n, = rl()
    a = rl()
    print((sum(a[::2]) + max(maxsum(b) for b in[
        [a[i] - a[i-1] for i in range(1, n, 2)],
        [a[i-1] - a[i] for i in range(2, n, 2)],
    ])))

