import sys

input = sys.stdin.readline

d, n = list(map(int, input().split()))
if n == 100:
    print((101 * 100**d))
    return
print((100**d * n))
