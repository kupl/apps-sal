from itertools import product
s=input()
a=0
for p in product((0,1),repeat=len(s)-1):
    t=s[0]
    for i,b in enumerate(p,start=1):
        if b==1:
            t+='+'+s[i]
        else:
            t+=s[i]
    a+=eval(t)
print(a)

