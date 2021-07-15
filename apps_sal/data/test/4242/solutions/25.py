# import math
# import statistics
# import itertools
# a=int(input())
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(int(i))
A,B,K= map(int,input().split())
# f = list(map(int,input().split()))
# g = [input().split for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen
count=0
wari=min(A,B)
while True:
    if A%wari==0 and B%wari==0:
        count+=1
    if count==K:
        print(wari)
        return
    wari-=1
