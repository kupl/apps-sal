# import math
# import statistics
# a=input()
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(i)
e1,e2 = map(str,input().split())
# f = list(map(int,input().split()))
#g = [input() for _ in range(a)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))
c=[]
count=0
ans=0
for i in range(int(e1),int(e2)+1):
    count=0
    for k in range(len(str(i))//2):
        if str(i)[k]==str(i)[-(k+1)]:
            count+=1
            if len(str(i))//2 == count:
                ans+=1

print(ans)
