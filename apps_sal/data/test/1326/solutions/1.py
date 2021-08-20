import sys
N = int(sys.stdin.readline())
ans = sum((N // x * (N // x + 1) * x // 2 for x in range(1, N + 1)))
print(ans)
