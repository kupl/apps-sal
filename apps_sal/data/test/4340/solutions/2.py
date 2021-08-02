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


n = int(input())
arr = inpmap()
for x in arr:
    print(x - 1 + x % 2, end=' ')
print()
