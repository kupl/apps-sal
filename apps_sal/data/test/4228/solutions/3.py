# import math
# import statistics
# import itertools
# a=int(input())
# b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(int(i))
N, L = list(map(int, input().split()))
# f = list(map(int,input().split()))
# g = [input().split for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen

azi2 = []
azi = [L + i for i in range(N)]
for i in azi:
    azi2.append(abs(i))
if 0 in azi:
    print((sum(azi)))
else:
    mi = azi2.index(min(azi2))
    del azi[mi]
    print((sum(azi)))
