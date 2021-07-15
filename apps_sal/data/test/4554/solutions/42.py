# import math
# import statistics
# import itertools
# a=int(input())
# b=input()
# c=[]
# for i in a:
#     c.append(int(i))
W,a,b= list(map(int,input().split()))
# f = list(map(int,input().split()))
# g = [int(input()) for _ in range(N)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen

ans1=b-(a+W)
ans2=a-(b+W)

if a+W<b or b+W<a:
    print((min(abs(ans1),abs(ans2))))
else:
    print((0))

