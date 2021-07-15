import sys
import io

stream_enable = 0

inpstream = """
3
2 1 3

"""

if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()

def inpmap():
    return list(map(int, input().split()))

n = int(input())
arr = inpmap()
arr.sort()
print(arr[len(arr) // 2 - (1 - n % 2)])

