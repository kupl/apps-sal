import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def solve():
    m, d, w = nm()
    g = w // gcd(d-1, w)
    c = min(m, d)
    v = c // g
    ans = v * (v - 1) // 2 * g
    ans += (c - g * v) * v
    print(ans)
    return


# solve()

T = ni()
for _ in range(T):
    solve()

