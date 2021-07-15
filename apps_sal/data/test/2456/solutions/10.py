read = lambda: map(int, input().split())
t = int(input())
for _ in range(t):
	n, r = read()
	x = min(n - 1, r)
	ans = x * (x + 1) // 2
	if r >= n: ans += 1
	print(ans)
