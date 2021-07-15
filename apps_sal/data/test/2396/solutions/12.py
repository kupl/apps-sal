n=int(input())
d={}
for i in range(n):
    s=input()
    s=s.replace('(','')
    s=s.replace(')','')
    s=s.split('/')
    c=float(s[-1])
    s=s[0]
    s=s.split('+')
    a=float(s[0])
    b=float(s[1])
    ans=(a+b)/c
    if ans in d:
        d[ans].append(i)
    else:
        d[ans]=[i]
l=[0]*n
for k in list(d.keys()):
    for i in d[k]:
        l[i]=str(len(d[k]))
print(' '.join(l))

