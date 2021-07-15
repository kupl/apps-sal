n=list(input())
s=''
if len(n)%2==0:
    while n!=[]:
        s+=n[-1]
        n.pop(-1)
        if n==[]:
            break
        s+=n[0]
        n.pop(0)
else:
    while n!=[]:
        s+=n[0]
        n.pop(0)
        if n==[]:
            break
        s+=n[-1]
        n.pop(-1)
print(s[::-1])

