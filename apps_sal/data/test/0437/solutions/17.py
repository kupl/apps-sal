import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
n = int(input())
ans = 0
for i in range(n, 0, -1):
    ans += 1 / i
print(ans)
