import sys, time, os
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

n, k = map(int, input().split())
min_x = n*k + 1

for i in range(1, k):
    if n % i == 0:
        min_x = min(min_x, n//i*k + i)
print(min_x)

##############################################
if __flag:
    stdout.close()
    stdin.close()

    print(time.time() - now, file=sys.stderr)

