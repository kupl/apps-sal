import sys
3


def input():
    return sys.stdin.readline().strip()


n = int(input())
ans = sum((i * (n - i + 1) for i in range(1, n + 1)))
for _ in range(n - 1):
    (u, v) = [int(x) for x in input().split()]
    ans -= min(u, v) * (n - max(u, v) + 1)
print(ans)
