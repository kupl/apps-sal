a=str(hex(int(input())))
b=0
for i in range(2,len(a)):
    if a[i]=="0" or a[i]=="4" or a[i]=="6" or a[i]=="9" or a[i]=="a" or a[i]=="d":
        b+=1
    elif a[i]=="8" or a[i]=="b":
        b+=2
print(b)

