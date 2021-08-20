import sys


def I():
    return sys.stdin.readline().rstrip()


t = int(I())
for _ in range(t):
    (n, r) = list(map(int, I().split()))
    x = list(map(int, I().split()))
    x.sort()
    ans = 0
    while len(x) > 0 and x[-1] > ans * r:
        y = x[-1]
        while len(x) > 0 and x[-1] == y:
            x.pop()
        ans += 1
    print(ans)
