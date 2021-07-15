N = int(input())
H = list(map(int,input().split()))

ans = 0
h = H[0]
for i in H:
	if h <= i :
		ans += 1
		h = i

print(ans)

