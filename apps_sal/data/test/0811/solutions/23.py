s=input().split(' ')
a=int(s[0])
b=int(s[1])
r=0
s=0
while (a>0):
    s=s+a
    new=(a+r)//b
    r=(a+r)%b
    a=new
    
print(s)
