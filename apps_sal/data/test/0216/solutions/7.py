from sys import stdin, stdout

n = int(stdin.readline())
first, second = 0, 0

values = list(map(int, stdin.readline().split()))
for v in values:
    if v >= 0:
        first += v
    else:
        second += v

stdout.write(str(first - second))
