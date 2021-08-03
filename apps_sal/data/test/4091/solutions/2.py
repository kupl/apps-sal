import sys
import io

stream_enable = 0

inpstream = """

"""

if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()


def inpmap():
    return list(map(int, input().split()))


n, k = inpmap()
arr = inpmap()
ar = arr[:]
ar.sort()
b = ar[-k:]
print(sum(b))
m = 0
r = []
for i, x in enumerate(arr):
    if x in b:
        b.remove(x)
        r.append(i - m + 1)
        m = i + 1
r[-1] += n - m
print(*r)
