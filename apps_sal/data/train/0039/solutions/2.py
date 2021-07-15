# from collections import defaultdict

for _ in range(int(input())):
	# n = int(input())
	a, b, p = map(int, input().split())
	s = input()
	n = len(s)
	money = [0] * n
	last = 'C'
	for i in range(n-2, -1, -1):
		if s[i] == last:
			money[i] = money[i+1]
		elif s[i] == 'A':
			money[i] = money[i+1] + a
		else:
			money[i] = money[i+1] + b
		last = s[i]

	for i in range(1, n+1):
		if money[i-1] <= p:
			print(i)
			break
