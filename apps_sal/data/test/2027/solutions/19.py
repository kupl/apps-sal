n=int(input())
a=input().split()
for i in range (n):
    a[i]=int(a[i])
a.reverse()
b=[]
b.append(a[0])
for i in range (n-1):
    b.append(a[i]+a[i+1])
b.reverse()
print(" ".join(map(str, b)))

