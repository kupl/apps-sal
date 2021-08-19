import sys
import math
a = 'abcdefghijklmnopqrstuvwxyz'
s = input()
pos = 0
vv = ord('a')
ans = 0
for i in s:
    gg = ord(i) - vv
    ans += min(int(math.fabs(gg - pos)), 26 - max(gg, pos) + min(pos, gg))
    pos = gg
print(ans)
