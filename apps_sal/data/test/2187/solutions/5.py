from sys import exit,stdin,stderr
def rl():
    return [int(w) for w in stdin.readline().split()]

T, = rl()
for _ in range(T):
    n, = rl()
    a = rl()
    r = 0
    for i in range(n - 1):
        d = a[i] - a[i+1]
        if d > 0:
            r += d
    print(r)

