from itertools import islice, cycle
import sys
from math import tan, pi

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__


def go():
    n = int(input())
    # a,b,c,d = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()

    return 1 / (tan(pi / (2 * n)))


# x,s = map(int,input().split())
t = int(input())
# t = 1
ans = []
for _ in range(t):
    # print(go())
    ans.append(str(go()))
#
print('\n'.join(ans))
