b=['a','b','c','d','e','f','g','h','i','j']
l=[0]*10
z=[]
n=int(input())
for i in range(n):
    s=input()
    z.append(s[0])
    for j in range(len(s)):
        l[b.index(s[j])]+=10**(len(s)-j-1)
s=0
h=0
j=1
for k in range(10):
    ma=0
    for i in range(10):
        if l[i]>ma:
            ma=l[i]
    bi=b[l.index(ma)]
    l[l.index(ma)]=0
    if not(bi in z) and h==0:
        h=1
    else:
        s+=ma*j
        j+=1  
print(s)
