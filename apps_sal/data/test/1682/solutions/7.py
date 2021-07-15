read=lambda:list(map(int,input().split()))
n,k=read()
a=list(read())
b=list(read())
c=[[a[i]-b[i],i] for i in range(len(a))]
c.sort()
s=0
i=0
A=[]
while i<len(a) and(c[i][0]<=0 or i<k):A.append(c[i][1]);i+=1
B=list(set([i for i in range(n)])-set(A))

print(sum([a[i] for i in A])+sum([b[i] for i in B]))



