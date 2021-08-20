import sys
import collections
lines = [s.rstrip('\n') for s in sys.stdin.readlines()]
(n,) = [int(num) for num in lines.pop(0).split(' ')]
blue_list = lines[:n]
lines = lines[n:]
(m,) = [int(num) for num in lines.pop(0).split(' ')]
red_list = lines
blue = collections.Counter(blue_list)
red = collections.Counter(red_list)
c = blue - red
lis = list(c.values())
if len(lis):
    ans = max(lis)
else:
    ans = 0
print(ans)
