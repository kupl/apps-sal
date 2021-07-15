def twos(m):
	rt = 0
	while m%2 == 0:
		m //= 2
		rt += 1
	return rt

n = int(input())
a = list(map(int,input().split()))
ans = 0
for j in a:
	ans += twos(j)
print(ans)
