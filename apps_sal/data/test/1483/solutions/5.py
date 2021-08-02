import sys
import io

stream_enable = 0

inpstream = """
3
2 3 2
"""

if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()


def inpmap():
    return list(map(int, input().split()))


n = int(input())
arr = [x - 1 for x in inpmap()]
for i in range(n):
    vis = [0] * n
    p = i
    while True:
        if vis[p]:
            print(p + 1, end=' ')
            break
        vis[p] = 1
        p = arr[p]
print()
