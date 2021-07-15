from sys import stdin
from math import ceil
s=stdin.readline().strip()
f1=False

for i in s:
    if i=="m" or i=="w":
        f1=True
        break
if f1:
    print(0)
    return
f=[0 for i in range(len(s)+4)]
f[0]=1
f[1]=1
mod =10**9+7
for i in range(2,len(s)+2):
    f[i]=(f[i-2]+f[i-1])%mod
arr=[1]
n=0
u=0
if s[0]=="n":
    n+=1
if s[0]=="u":
    u+=1
for i in range(1,len(s)):
    if s[i]=="n" and s[i-1]=="n":
        n+=1
    elif s[i]=="u" and s[i-1]=="u":
        u+=1
    elif s[i]=="u":
        u=1
    elif s[i]=="n":
        n=1
    if s[i-1]=="n" and s[i]!="n":
        
        arr.append(n)
        n=0
    if s[i-1]=="u" and s[i]!="u":
        arr.append(u)
        u=0
if s[-1]=="n":
    arr.append(n)
if s[-1]=="u":
    arr.append(u)
        
ans=1
for i in range(len(arr)):
    ans=(ans*f[arr[i]])%mod
print(ans)

