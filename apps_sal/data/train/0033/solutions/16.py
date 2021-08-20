import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    n = int(input())
    print(2)
    x = n
    for i in range(n - 1, 0, -1):
        print(x, i)
        x = (x + i + 1) // 2
