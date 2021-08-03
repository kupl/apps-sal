import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
def listin(): return list(map(int, input().split()))
def mapin(): return map(int, input().split())


for _ in range(int(input())):
    n, m = map(int, input().split())
    if n - m == 1:
        print("NO")
    else:
        print("YES")
