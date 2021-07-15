def main():
	n, d = map(int, input().split())
	a = list(map(int, input().split()))
	
	pref, mx, add, ans = [0] * n, [0] * n, 0, 0

	for pos in range(n):
		pref[pos] = a[pos] if not pos else a[pos] + pref[pos-1]

	for pos in range(n-1, -1, -1):
		mx[pos] = pref[pos] if pos == n - 1 else max(mx[pos + 1], pref[pos])

	for i in range(n):
		if pref[i] + add > d:
			print("-1")
			return
		if a[i] == 0 and pref[i] + add < 0:
			ans += 1
			add += max(-(pref[i] + add), d - mx[i] - add)
	print(ans)

def __starting_point():
	main()
__starting_point()
