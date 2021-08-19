from sys import stdin
(n, a, b) = list(map(int, stdin.readline().split()))
apples1 = list(map(int, stdin.readline().split()))
apples2 = list(map(int, stdin.readline().split()))
for i in range(1, n + 1):
    if i in apples1:
        print(1, end=' ')
    else:
        print(2, end=' ')
