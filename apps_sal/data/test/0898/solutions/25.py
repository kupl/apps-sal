import bisect
N,M=map(int,input().split())
divd=[]
i=1
while i*i<=M:
    if M%i==0:
        divd.append(i)
        if i!=M//i:
            divd.append(M//i)
    i+=1
divd.sort()
k=bisect.bisect_left(divd,N)
print(M//divd[k])
