b=int(input())
g=int(input())
n=int(input())
l=[]
count=0
for i in range(n+1):
    x1=i
    x2=n-i
    if (x1<=b and x2<=g):
        count+=1
    else:
        continue
print(count)
