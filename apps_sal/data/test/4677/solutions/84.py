import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

s = input()

ans = ''
for i in range(len(s)):
    if s[i] == 'B':
        if len(ans) == 0: continue
        ans = ans[0:-1]
    else:
        ans += s[i]
print(ans)
