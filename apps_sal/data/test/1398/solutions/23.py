import sys
from bisect import bisect_left, bisect_right


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def input():
    return sys.stdin.readline().strip()


sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n = int(input())
arr = get_array()
arr.sort()
maxi = -1
for i in range(n):
    x = bisect_right(arr, 2 * arr[i])
    x -= 1
    maxi = max(maxi, x - i + 1)
print(n - maxi)
