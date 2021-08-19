import sys
import math
mod = 10 ** 9 + 7


def solve(test_index):
    (a, b) = list(map(int, input().split()))
    ans = math.ceil(abs(a - b) / 10)
    print(ans)
    return


if 'PyPy' not in sys.version:
    sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(100000)
num_tests = 1
num_tests = int(input())
for test in range(1, num_tests + 1):
    solve(test)
