s=input()
c=[0]*26
for i in s:
    c[ord(i)-97]+=1
t=[]
u=[]
for i in s:
    t.append(i)
    c[ord(i)-97]-=1
    while t and sum(c[:(ord(t[-1])-97)])==0:
        u.append(t.pop())
        
print(''.join(u))      
