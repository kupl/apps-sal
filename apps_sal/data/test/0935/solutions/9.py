enter=input()
l=enter.split()
m=int(l[0])
n=int(l[1])
x=min(m,n)
y=x%2
if y==0:
    print("Malvika")
if y==1:
    print("Akshat")

