def main():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))

	s = a[0]
	for l in range(n):
		for r in range(l,n):
			out = sorted(a[:l] + a[r+1:], reverse=True)
			inside = sorted(a[l:r+1])
			temp = sum(a[l:r+1])
			for i in range(min(k, len(out), len(inside))):
				if out[i] > inside[i]:
					temp += out[i] - inside[i]
				else:
					break
			if temp > s:
				s = temp
	print(s)

main()
