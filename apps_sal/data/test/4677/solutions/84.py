import math
import collections
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


s = input()

ans = ''
for i in range(len(s)):
    if s[i] == 'B':
        if len(ans) == 0:
            continue
        ans = ans[0:-1]
    else:
        ans += s[i]
print(ans)
