
import sys
# sys.stdin=open("data.txt")
input = sys.stdin.readline

n, k = list(map(int, input().split()))

ans = 0
for i in sorted(map(int, input().split())):
    while i > 2 * k:
        ans += 1
        k *= 2
    k = max(k, i)

print(ans)
