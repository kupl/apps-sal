import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
x = int(input())
ans = 0
q = x // 11
r = x % 11
ans += q * 2
if r == 0:
    pass
elif r <= 6:
    ans += 1
else:
    ans += 2
print(ans)
