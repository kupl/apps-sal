for _ in range(int(input())):
	n = int(input())
	l = [int(input()) for a in range(n)]
	ans = 0
	for i in range(n):
		if l[i] in l[i+1:]:
			ans += 1
			while l[i] in l[i+1:] + l[:i]:
				l[i] += 1000
				l[i] %= 10000
	print(ans)
	for i in l:
		print("%04d" % i)

