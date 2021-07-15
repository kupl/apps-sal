s=input()
x=s.index('^')
ans=0
for i in range(len(s)):
    if(s[i]=='=' or s[i]=='^'):
        continue
    if(i<x):
        ans+=int(s[i])*(x-i)
    else:
        ans-=int(s[i])*(i-x)
if(ans==0):
    print("balance")
elif(ans>0):
    print("left")
else:
    print("right")
