from sys import exit,stdin,stderr
def rl():
    return [int(w) for w in stdin.readline().split()]

T, = rl()
for _ in range(T):
    n,k = rl()
    a = rl()
    d = max(a)
    a = [d - x for x in a]
    if k % 2 == 0:
        d = max(a)
        a = [d - x for x in a]
    print(*a)

