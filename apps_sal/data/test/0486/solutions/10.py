n=input()
q=len(n)-1
ma=9**q
q=1
for i in range(len(n)):
    if n[i]!='0':
        e=q
        e*=(int(n[i])-1)
        e*=9**(len(n)-i-1)
        ma=max(ma, e)
    q *= int(n[i])
w=1
for i in n:
    w*=int(i)
print(max(ma, w))
