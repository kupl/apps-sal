import sys
# from collections import defaultdict
t = 1
t = int(input())
for i in range(t):
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    # a=list(map(int,sys.stdin.readline().strip().split()))
    # b=list(map(int,sys.stdin.readline().strip().split()))
    # d = defaultdict(int)
    print((24 - n - 1) * 60 + 60 - m)
