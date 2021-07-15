s=input()
c=input()
i=0
while s[i] in c:
    c=c[c.index(s[i])+1:]
    i+=1
print(i+1)

