import sys
input = sys.stdin.readline

n=int(input())
l=[0]*26
for i in range(n):
	s=input()
	l[ord(s[0])-97]+=1

ans=0
for i in range(26):
	cur=l[i]//2
	nex=l[i]-cur
	ans+=cur*(cur-1)//2
	ans+=nex*(nex-1)//2

print(ans)

