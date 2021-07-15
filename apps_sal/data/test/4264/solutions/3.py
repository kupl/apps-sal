n=int(input())
cnt=0
for i in range(n):
	if len(str(i+1))%2==1:
		cnt=cnt+1
print(cnt)

