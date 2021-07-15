n, b, d= [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
k = 0
ans = 0
for i in s:
	if i <= b:
		k+=i
		if k > d:
			ans +=1
			k= 0
print(ans)

