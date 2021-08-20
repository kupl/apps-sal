import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
ans = 1
for i in range(0, n):
    if (ans + 1) ** 2 > n:
        break
    ans += 1
print(ans ** 2)
