from collections import Counter


def main():
	n = int(input())
	a = input()
	b = input()
	a1, b1 = a[::-1], b[::-1]
	n2 = n // 2
	if n % 2 and a[n2] != b[n2]:
		res = 1
	else:
		res = 0
	for i in range(n2):
		ai, a1i = a[i], a1[i]
		bi, b1i = b[i], b1[i]
		if bi == b1i:
			if ai != a1i:
				res += 1
			continue
		cnt1 = Counter((ai, a1i))
		cnt2 = Counter((bi, b1i))
		res += sum((cnt1 - cnt2).values())
	print(res)


main()

