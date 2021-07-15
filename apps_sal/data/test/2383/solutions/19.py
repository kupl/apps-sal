import math
import statistics
a=int(input())
#b=int(input())
# c=[]
# for i in b:
#     c.append(i)
# e1,e2 = map(int,input().split())
f = list(map(int,input().split()))
#j = [input() for _ in range(3)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))
ans=0
count=0
for i in range(a):
    if ans+1 == f[i]:
        ans=f[i]
        count+=1
if count>0:   
    print(len(f)-count)
else:
    print(-1)
