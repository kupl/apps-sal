from math import gcd
for i in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	a.sort(reverse=True)

	answer = []
	answer.append(a.pop(0))
	n -= 1
	gc = answer[0]
	for _ in range(n):
		index = 0
		m = 0
		for i, val in enumerate(a):
			num = gcd(gc, val)
			if num >= m:
				m = num
				index = i
		gc = min(gc, m)
		if gc == 1:
			answer.extend(a)
			break
		else:
			answer.append(a.pop(index))
	print(" ".join(str(num) for num in answer))
