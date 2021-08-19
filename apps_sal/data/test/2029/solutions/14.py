from collections import deque
import sys
import time
import os
from pprint import pprint as pp
if os.environ.get('_ONPC_', False):
    stdin = open('input.txt', 'r')
    stdout = open('output.txt', 'w')
    sys.stdin = stdin
    sys.stdout = stdout

    now = time.time()
    __flag = True
else:
    __flag = False


def what(obj):
    if __flag:
        pp(obj, sys.stderr)


#############################################
n, s = map(int, input().split())

d = {}

for i in range(n - 1):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
    if b not in d:
        d[b] = 1
    else:
        d[b] += 1

cnt = 0
for e in d:
    if d[e] == 1:
        cnt += 1

print(2 * s / cnt)

##############################################
if __flag:
    stdout.close()
    stdin.close()

    print(time.time() - now, file=sys.stderr)
