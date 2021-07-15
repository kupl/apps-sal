import bisect
n,m=map(int,input().split())
rid=[None for i in range(n)]
tax=[None for i in range(m)]
res=[0 for i in range(m)]
ss=input().split()
s=input().split()
indrid=0
indtax=0
for i in range(n+m):
    if s[i]=="0":
        rid[indrid]=int(ss[i])
        indrid+=1
    else:
        tax[indtax]=int(ss[i])
        indtax+=1
for x in rid:
    ind=bisect.bisect_left(tax,x)
    if ind==0:
        res[0]+=1
        continue
    if ind==m:
        res[m-1]+=1
        continue
    if tax[ind]-x<x-tax[ind-1]:
        res[ind]+=1
    else:
        res[ind-1]+=1
for i in res:
    print(i,end=" ")
print("")

