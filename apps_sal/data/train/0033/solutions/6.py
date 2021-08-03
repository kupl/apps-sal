import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    print(2)
    if n == 2:
        print(1, 2)
    else:
        print(n, n - 2)
        print(n - 1, n - 1)
        for j in range(n - 3):
            print(n - 1 - j, n - 1 - j - 2)
