table=[]
for i in range(0,64):
    ans=-1
    for z in bin(i):
        if z=='0':
            ans+=1
    table.append(ans+8-len(bin(i)))
s=input()
ans=1
for i in s:
    if i=="_":
        z=63
    elif i=="-":
        z=62
    elif i.isdigit():
        z=int(i)
    elif ord(i)>=97:
        z=ord(i)-97+36
    else:
        z=ord(i)-65+10
    ans*=3**table[z]
    ans%=(10**9+7)
print(ans)

