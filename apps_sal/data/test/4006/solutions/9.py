import sys
input = sys.stdin.readline
n = int(input())
visited = set()


def f(n):
    n = n + 1
    while n % 10 == 0:
        n /= 10
    return n


ans = 0
while f(n) not in visited:
    visited.add(n)
    n = f(n)
    ans += 1
print(ans + 1)
