import sys
sys.setrecursionlimit(10**6)

n = int(input())
d = [int(input()) for i in range(n)]

print((len(set(d))))
