import sys
import math
# sys.stdin = open("in.txt")
for _ in range(int(input())):
    n = int(input())
    li = sorted(list(map(int, input().split())))
    was = 0
    for i in range(n - 1):
        if li[i + 1] - li[i] == 1:
            was = 1
    if was:
        print(2)
    else:
        print(1)
