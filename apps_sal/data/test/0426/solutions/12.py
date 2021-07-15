def gns():
    return list(map(int,input().split()))
n,k=gns()
s=input()

if k==0:
    print(s)
    quit()
if len(s)==1:
    print(0)
    quit()

s=[int(x) for x in s]
if s[0]>1:
    k-=1
    s[0]=1
for i in range(1,n):
    if k==0:
        break
    if s[i]==0:
        continue
    s[i]=0
    k-=1
print(''.join(map(str,s)))



