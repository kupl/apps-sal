import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    while n > 0 and x // 2 + 10 < x:
        x = x // 2 + 10
        n -= 1
    print('YES' if x <= 10 * m else 'NO')
