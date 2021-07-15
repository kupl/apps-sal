# import math
# import statistics
# import itertools
# a=int(input())
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(int(i))
N,A,B= list(map(int,input().split()))
# f = list(map(int,input().split()))
# g = [input().split for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen
count=0
ans=[]
for i in range(1,N+1):
    cal=[]
    for k in str(i):
        cal.append(int(k))

    if A<=sum(cal)<=B:
        ans.append(i)
        
print((sum(ans)))
            

