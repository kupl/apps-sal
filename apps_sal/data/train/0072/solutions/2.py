import sys

stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: list(map(int, stdin.readline().split()))
nl = lambda: list(map(int, stdin.readline().split()))

def solve():
    n, k = nm()
    a = nl()
    if k < len(set(a)):
        print(-1)
        return
    f = list(set(a))
    f += [1]*(k-len(f))
    f *= n
    print(len(f))
    print(*f)
    return


t = ni()
for _ in range(t):
    solve()

