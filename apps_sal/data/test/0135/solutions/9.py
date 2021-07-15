s=input()
s=s.split()
n=int(s[0])
k=int(s[1])
b=1
a=[]
for i in range(1,k+1):
    c=n%i
    a.append(c)
    if c in a[:-1]:
        print('No')
        b=0
        break
if b==1:
    print('Yes')

