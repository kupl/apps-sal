tc = int(input())

while tc > 0:
	tc -= 1
	n = int(input())
	p = [0] + list(map(int, input().split()))

	ans = [0] * (n + 1)
	mk = [False] * (n + 1)

	for i in range(1 , n + 1):
		if not mk[i]:
			sz = 1
			curr = p[i]
			mk[i] = True
			while curr != i:
				sz += 1
				mk[curr] = True
				curr = p[curr]

			ans[i] = sz
			curr = p[i]
			while curr != i:
				ans[curr] = sz
				curr = p[curr]

	print(" ".join([str(x) for x in ans[1:]]))



