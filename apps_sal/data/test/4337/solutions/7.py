import sys
import collections
lines = [s.rstrip('\n') for s in sys.stdin.readlines()]
(n,) = [int(num) for num in lines.pop(0).split(' ')]
s_list = lines.pop(0).split(' ')
c = collections.Counter(s_list)
if len(c) == 3:
    print('Three')
elif len(c) == 4:
    print('Four')
