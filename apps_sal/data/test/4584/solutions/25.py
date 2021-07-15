# import math
# import statistics
a=int(input())
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#    c.append(i)
# e1,e2 = map(int,input().split())
f = list(map(int,input().split()))
#g = [input() for _ in range(a)]

f.sort()
count=1
ans=[0 for i in range(a)]

for i in range(len(f)-1):
    if f[i]==f[i+1]:
        count+=1
    else:
        ans[f[i]-1]=count
        count=1
if count>=1:
    ans[f[-1]-1]=count
for i in ans:
    print(i)
