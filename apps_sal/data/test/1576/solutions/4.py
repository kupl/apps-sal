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

s = input().strip()

ans = ''

while s:
    if len(s) & 1:
        ans = s[0] + ans
        s = s[1:]
    else:
        ans = s[-1] + ans
        s = s[:-1]

print(ans)

##############################################
if __flag:
    stdout.close()
    stdin.close()

    print(time.time() - now, file=sys.stderr)

