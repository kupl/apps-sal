# import math
# import statistics
# import itertools
a = int(input())
# b=input()
# c=[]
# for i in a:
#     c.append(int(i))
# A,B,C= map(int,input().split())
f = list(map(int, input().split()))
# g = [int(input()) for _ in range(N)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen

count = 0
ma = 0
ans = {}

for i in range(len(f) - 1):
    if f[i + 1] <= f[i]:
        count += 1
    else:
        ma = max(ma, count)
        count = 0

if count >= 1:
    ma = max(ma, count)

print(ma)
