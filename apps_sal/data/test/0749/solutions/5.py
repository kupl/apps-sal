import math
s=input()
e=set()
for i in s:
    e.add(i)
d={}
for i in e:
    d[i]=[-1]
if len(d)==len(s):
    print(math.ceil((len(s)+1)/2))
    return
a=[]
for i in range(len(s)):
    d[s[i]].append(i)
for i in d:
    d[i].append(len(s))
q=-1
ans=1221243214
for i in d:
    q=-1
    for j in range(1,len(d[i])):
        q=max(q,d[i][j]-d[i][j-1])
    ans=min(q,ans)
print(ans)

