import sys

readline = sys.stdin.readline
read = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def solve():
    a, b = nm()
    if a < b:
        a, b = b, a
    if a > b*2:
        print(b)
    else:
        res = a - b
        a -= 2 * res
        b -= res
        res += (b // 3) * 2
        a %= 3
        if a > 1: res += 1
        print(res)
    return


# solve()

T = ni()
for _ in range(T):
    solve()

