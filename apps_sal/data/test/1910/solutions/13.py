import sys
n = int(sys.stdin.readline())
m = (n - 3) * 9 * 4 ** (2 * n - 2 - (n + 2)) + 2 * 3 * 4 ** (2 * n - 2 - (n + 1))
print(int(4 * m))
