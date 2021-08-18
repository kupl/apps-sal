import sys

for _ in range(int(input())):
    a, b, c = sorted(list(map(int, input().split())))
    print((a + b + c - max(0, c - (a + b))) // 2)
