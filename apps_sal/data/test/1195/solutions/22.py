import sys
import math
import queue
sys.setrecursionlimit(1000000)
n = int(input())
a = list(map(int, input().split()))
print((a[2] ^ min(a)) + 2)
