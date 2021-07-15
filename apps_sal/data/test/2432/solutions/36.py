x=bin(int(input()))[2:]

x="0"*(6-len(x))+x
x1=list(x)
temp=x1[1]
x1[1]=x1[5]
x1[5]=temp
temp=x1[2]
x1[2]=x1[3]
x1[3]=temp
x2="".join(x1)
print(int(x2,2))
