n=int(input())
c=input()
i=0
s=0
while i<len(c):
    if i<len(c)-1:
        if c[i+1]!=c[i]:
            s+=1
            i+=2
        else:
            s+=1
            i+=1
    else:
        s+=1
        break
print(s)
        

