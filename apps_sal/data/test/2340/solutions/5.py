import sys


def I():
    return sys.stdin.readline().rstrip()


q = int(I())
for _ in range(q):
    h, n = list(map(int, I().split()))
    p = list(map(int, I().split()))
    i, ans = 0, 0
    while i < n:
        if h == p[i]:
            pass
        elif p[i] == 1:
            h = 0
        elif i < n - 1 and p[i] - 1 == p[i + 1]:
            h = p[i + 1]
        else:
            ans += 1
            h = p[i] - 1
        i += 1
    print(ans)
