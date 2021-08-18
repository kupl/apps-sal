import sys
import math
# sys.stdin = open("in.txt")
n, p = map(int, input().split())
for i in range(1, 1000000):
    if n - p * i >= i and bin(n - p * i)[2:].count("1") <= i:
        print(i)
        return
print(-1)
