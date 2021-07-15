s=list(input())
a,b=list(map(int,input().split()))
l=len(s)
s1=[0]*(l+1)
s2=[0]*(l+1)
for i in range(l):
	s[i]=ord(s[i])-ord('0')
p=1
for i in range(l-1,-1,-1):
	s1[i]=(s1[i+1]+s[i]*p)%b
	p=(p*10)%b
p=0
for i in range(l-1):
	p=(p*10+s[i])%a
	if p==0 and s1[i+1]==0 and s[i+1]:
		print("YES")
		print(''.join(map(str,s[:i+1])))
		print(''.join(map(str,s[i+1:])))
		return
print("NO")

