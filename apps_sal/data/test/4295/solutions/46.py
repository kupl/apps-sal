# import math
# import statistics
# import itertools
# a=int(input())
# b=input()
# c=[]
# for i in a:
#     c.append(int(i))
N, K = map(int, input().split())
# f = list(map(int,input().split()))
# g = [int(input()) for _ in range(N)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen

if N % K == 0:
    print(0)
else:
    et = N // K
    a1 = et * K
    a2 = (et + 1) * K
    mi = min(abs(a1 - N), abs(a2 - N))
    print(mi)
