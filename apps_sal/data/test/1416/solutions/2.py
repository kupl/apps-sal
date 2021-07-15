n,w=map(int,input().split(" "))
mas=list(map(int,input().split(" ")))
mas.sort()
x1=w/n/3
x2=mas[0]
x3=mas[n]/2
print(3*n*min(x1,x2,x3))
