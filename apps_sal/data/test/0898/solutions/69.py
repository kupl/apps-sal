n,m=map(int,input().split())
a=[]
for i in range(1,int(m**.5)+1):
    if m%i==0:
        if m//i>=n:a+=[i]
        if i>=n:a+=[m//i]
print(max(a))
