import bisect
n,m=map(int,input().split(' '))
a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
a.sort()
ans=[]
for i in b:
    ans.append(bisect.bisect(a,i))
print(str(ans).replace('[', '').replace(']', '').replace(',', ''))
