import sys
input = sys.stdin.readline

d, n = map(int, input().split())

if d == 0:
    if n < 100:
        print(n)
    else:
        print(101)
elif d == 1:
    if n < 100:
        print(n * 100)
    else:
        print(101 * 100)
else:
    if n < 100:
        print(n * 10000)
    else:
        print(101 * 10000)
