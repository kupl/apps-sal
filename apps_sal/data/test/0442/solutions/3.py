from collections import deque, defaultdict
import math
import sys
import string
import bisect
import heapq
input = sys.stdin.readline
def L(): return list(map(int, input().split()))
def Ls(): return list(input().split())
def M(): return list(map(int, input().split()))
def I(): return int(input())


n = I()
if(n % 2 == 0 or n <= 3):
    print("NO")
else:
    print(1, (n - 3) // 2)
