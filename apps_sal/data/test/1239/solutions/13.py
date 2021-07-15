x=int(input())
y=input()
a=[int(i) for i in y.split()]
a.sort()
b=[]
i=0
while i<len(a)-1:
    b.append(abs(a[i]-a[i+1]))
    i+=1
print(min(b),b.count(min(b)))

