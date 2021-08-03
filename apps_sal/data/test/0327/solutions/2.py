from sys import stdin, stdout

n, k = list(map(int, stdin.readline().rstrip().split()))

if k == 1:
    print(n)
else:
    x = 1
    while 2 * x <= n:
        x *= 2
    print(2 * x - 1)
