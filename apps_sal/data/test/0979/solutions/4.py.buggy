from collections import deque
import sys
input = sys.stdin.readline

n, MOD = list(map(int, input().split()))
a = list(map(int, input().split()))
if n > MOD:
    print(0)
    return

ans = 1
for i in range(n):
    for j in range(i + 1, n):
        ans *= abs(a[i] - a[j])
        ans %= MOD
print(ans)
