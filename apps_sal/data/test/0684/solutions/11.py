"""
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
"""

testcases = int(input())

for case in range(testcases):
    (a,b,c,d)  = [int(zax) for zax in input().split()]
    print(b,c,c)
