def main():
	m, d = map(int, input().split())
	a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	num = a[m - 1]
	ans = 1
	num -= (8 - d)
	ans += ((num + 7 - 1) // 7)
	print(ans)

main()
