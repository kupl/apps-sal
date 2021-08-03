import sys

K, S = map(int, sys.stdin.readline().split())
ans = 0
for x in range(K + 1):
    for y in range(K + 1):
        if 0 <= S - (x + y) <= K:
            ans += 1
print(ans)
