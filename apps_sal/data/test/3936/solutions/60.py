n=int(input())
s1=input()
a2=input()

s=list(s1)
t=[]

if len(s)==1:
    print((3))
    return

if len(s)==2:
    print((6))
    return


for i in range(1,len(s)-1):
    if s[i]==s[i+1] and s[i]!=s[i-1]:
        t.append(2)
    if s[i]!=s[i+1] and s[i]!=s[i-1]:
        t.append(1)

if s[0]==s[1]:
    t=[2]+t
else:
    t=[1]+t

if s[len(s)-1]!=s[len(s)-2]:
    t.append(1)


if t[0]==1:
    ans=3
else:
    ans=6

for i in range(1,len(t)):
    if t[i]==1:
        if t[i-1]==1:
            ans*=2
        else:
            ans*=1
    if t[i]==2:
        if t[i-1]==1:
            ans*=2
        else:
            ans*=3

print((ans%1000000007))

