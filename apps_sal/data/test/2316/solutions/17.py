import sys
def I():
    return sys.stdin.readline().rstrip()

for _ in range(int(I())):
    x, n, m = list(map(int, I().split()))
    while n > 0 and x > 20:
        x = x // 2 + 10
        n -= 1
    print("YES" if x <= m * 10 else "NO")

