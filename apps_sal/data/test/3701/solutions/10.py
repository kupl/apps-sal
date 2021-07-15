from functools import cmp_to_key

s=input()
s=s.split(" ")
n=int(s[0])
x=int(s[1])
y=int(s[2])
s=input()
s=list(s)
s.append('2')
p=0
for i in range(1,len(s)):
    if s[i]!='0' and s[i-1]=='0':
        p+=1
if p==0:
    print(0)
else:
    print((p-1)*min(x,y)+y)


