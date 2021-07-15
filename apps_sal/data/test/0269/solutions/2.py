def main():
	s = list(input())

	ans = []
	for c in "RBYG":
		x = s.index(c)
		x %= 4
		cn = 0
		while (x < len(s)):
			if (s[x] == '!'):
				cn += 1
			x += 4
		ans.append(cn)
	print(*ans)


main()
