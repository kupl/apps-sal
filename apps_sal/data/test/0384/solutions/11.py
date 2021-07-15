n=int(input())
s=input()
s=s+"W"
l=[]
q=0
for i in range(len(s)):
    if s[i]=="B":
        q=q+1
    else:
        if q!=0:
            l.append(q)
        q=0
print(len(l))
for i in range(len(l)):
    print(str(l[i])+" ",end="")


