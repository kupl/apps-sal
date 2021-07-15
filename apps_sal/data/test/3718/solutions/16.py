n=int(input())
l=sorted(set(map(int,input().split())))
for i in range(1,len(l)-1):
    if l[i]-l[i-1]==1 and l[i+1]-l[i]==1: print('YES'); break
else: print('NO')
