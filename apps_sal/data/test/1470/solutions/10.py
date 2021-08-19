import sys
import bisect
input = sys.stdin.readline
x = int(input())
ans = 2 * (x // 11)
if 0 < x % 11 <= 6:
    ans += 1
elif x % 11 > 6:
    ans += 2
print(ans)
