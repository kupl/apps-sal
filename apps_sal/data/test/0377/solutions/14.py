# import sys
# sys.stdin = open("#input.txt", "r")
n, m = list(map(int, input().split()))

if n == m:
    print(0)
elif m <= 1 or n - m <= 1:
    print(1)
else:
    print(min(m, n - m))
