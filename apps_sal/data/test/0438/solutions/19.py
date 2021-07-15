n=int(input())
s=''
i=0
while True:
    i+=1
    n-=i
    if n>i:
        s+=str(i)+' '
    else:
        s+=str(n+i)
        break
print(i)
print(s)
