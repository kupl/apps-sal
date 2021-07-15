n=int(input())
s=list(input())
sw=[0]
se=[0]
swc=0
sec=0
for i in range(n):
    if s[i]=='W':
        swc+=1
    else:
        sec+=1
    sw.append(swc)
    se.append(sec)
m=n
for i in range(n+1):
    m=min(m,sw[i]+se[-1]-se[i])
print(m)
