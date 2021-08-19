import sys
import io
stream_enable = 0
inpstream = '\ncodeforces\nyes\n'
if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()


def inpmap():
    return list(map(int, input().split()))


a = input()
b = input()
k = len(a) + len(b)
for i in range(min(len(a), len(b))):
    if a[-i - 1] == b[-i - 1]:
        k -= 2
    else:
        break
print(k)
