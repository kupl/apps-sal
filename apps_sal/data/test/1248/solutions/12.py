def main():
	d1, d2, d3 = list(map(int, input().split()))

	s = min(d1, d2 + d3) + min(d3, d1 + d2) + min(d2, d3 + d1)

	return s

print(main())

