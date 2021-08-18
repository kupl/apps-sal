
import sys

N = int(input())
h = [0] + list(map(int, input().split()))

ans = 0

for i in range(1, N + 1):
    d = h[i] - h[i - 1]
    ans += max(d, 0)

print(ans)
