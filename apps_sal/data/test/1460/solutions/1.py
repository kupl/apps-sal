import sys
input = sys.stdin.readline
n = int(input())
print(3 * n + 4)
print(0, 0)
for i in range(n + 1):
    print(i + 1, i + 1)
    print(i, i + 1)
    print(i + 1, i)
