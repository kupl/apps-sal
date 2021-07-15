n=int(input())
s=input()
a=1
x=s[0]
for i in range(1,n):
    if s[i]==x:a+=1
    else: break
b=1
x=s[-1]
for i in range(n-2,-1,-1):
    if s[i]==x:b+=1
    else: break
o=a+b+1
if s[0]==s[-1]:o+=a*b
print(o%998244353)
