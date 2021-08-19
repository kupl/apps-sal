import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N = int(input())
ans = 0
for (i, j) in zip(list(range(2, N + 1)), list(range(3, N + 1))):
    ans += i * j
print(ans)
