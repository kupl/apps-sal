# import math
# import statistics
# import itertools
a=int(input())
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(int(i))
# e1,e2,e3,e4 = map(int,input().split())
#f = list(map(int,input().split()))
g = [int(input()) for _ in range(a)]

ma = max(g)
del g[g.index(ma)]
print(int(sum(g)+ma/2))
