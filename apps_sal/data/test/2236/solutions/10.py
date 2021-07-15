input()
l = list(map(int,input().split()))
d={}
sum=0
for I in range(len(l)):
 if sum not in d:
  d[sum]=0
 d[sum]  +=1
 sum += l[I]
a=-100000
for I in d:
 a=max(a,d[I])
print(len(l)-a)
