import sys
if False:
    inp = open('A.txt', 'r')
else:
    inp = sys.stdin
(n, m) = map(int, inp.readline().split())
bulbs = []
for i in range(n):
    bulbs += list(map(int, inp.readline().split()))[1:]
bulbs = set(bulbs)
if len(bulbs) == m:
    print('YES')
else:
    print('NO')
