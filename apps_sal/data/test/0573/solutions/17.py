n=int(input()); d={}
a=input().split()
x=a.count('1')
y=a.count('2')
if y<x:
    print(y+int((x-y)/3))
else:
    print (x)

        

