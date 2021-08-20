import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    (n, m) = list(map(int, input().split()))
    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(m * 2)
