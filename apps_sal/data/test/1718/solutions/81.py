from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N, K = map(int, input().split())
A = inpl()
N -= 1
K -= 1
print((N + K - 1) // K)
