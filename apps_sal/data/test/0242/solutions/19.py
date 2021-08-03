import collections
import math

#a, b, c = map(int, input().split())
n = int(input())
i, ans = 0, 0
while i < n:
    ans += 5
    x = ans
    while x % 5 == 0:
        i += 1
        x //= 5

    if i > n:
        print(0)
        return
print(5)
print(ans, ans + 1, ans + 2, ans + 3, ans + 4, sep=' ')
