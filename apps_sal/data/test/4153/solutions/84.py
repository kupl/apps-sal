a=list(input())
temp1=0
temp0=0

for i in range(len(a)):
    if a[i]=="0":
        temp0+=1
    else:
        temp1+=1
print((min(temp0,temp1)*2))

