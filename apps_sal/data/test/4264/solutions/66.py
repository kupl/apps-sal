# import math
# import statistics
# import itertools
a = int(input())
# b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(int(i))
# H,W,K= map(int,input().split())
# f = list(map(int,input().split()))
# g = [input().split for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen

lis = [str(i) for i in range(1, a + 1)]

count = 0
for i in lis:
    if int(len(i)) % 2 != 0:
        count += 1
print(count)
