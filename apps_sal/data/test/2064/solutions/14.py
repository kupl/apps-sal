n = int(input())
ans = ''
if n % 2 == 0:
	for i in range(n//2):
		ans += '1'
else:
	ans += '7'
	for i in range(n//2-1):
		ans += '1'
	
print(ans)
