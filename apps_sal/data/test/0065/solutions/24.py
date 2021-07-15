n=int(input())
a=list(map(int, input().split()))
min_a = min(a)
ans = 1000000000000000000
prev_idx = -1000000000000000
for i in range(n):
	if a[i] == min_a:
		ans = min(ans, i-prev_idx)
		prev_idx = i
print(ans)
