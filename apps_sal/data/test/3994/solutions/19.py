n=int(input())
s=[int(i) for i in input()]
a=[]
b=[]
for i in range(n):
    c,d=map(int,input().split())
    a+=[c]
    b+=[d]
k=sum(s)
for j in range(10000):
    l=0
    for i in range(n):
        if j<b[i]:
            l+=s[i]
        else:
            l+=(1+s[i]+int((j-b[i])/a[i]))%2
    if l>k:
        k=l
print(k)
