n = int(input())
c = sorted(list(map(int,input().split())))
last = 0
ans = 0
for i in (c):
	if(last>i):
		continue
	elif(last<i-1):
		last = i-1
		ans+=1
	elif(last==i-1):
		last = i
		ans+=1
	else:
		last = i+1
		ans+=1
print(ans)

