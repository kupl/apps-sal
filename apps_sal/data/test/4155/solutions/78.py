N=int(input())
H=list(map(int, input().split()))

now=0
ans=0

for h in H:
	if now<h:
		ans+=h-now
	now=h

print(ans)
