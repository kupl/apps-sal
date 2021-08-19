import sys
input = sys.stdin.readline
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
for (a, b) in AB:
    L = [a, b]
    m = min(L)
    l = max(L)
    if (a + b) % 3 == 0 and l <= m * 2:
        print('YES')
    else:
        print('NO')
