q = int(input())
for rwre in range(q):
	n, m = map(int,input().split())
	l = list(map(int,input().split()))
	if m < n:
		print(-1)
	else:
		ll = [[l[i], i+1] for i in range(n)]
		ll.sort()
		l.sort()
		suma = 0
		if n == 2:
			print(-1)
		else:
			for i in range(n):
				suma += (l[i-1] + l[i])
			s1 = ll[0][1]
			s2 = ll[1][1]
			print(suma + (m-n)*(ll[0][0]+ll[1][0]))
			for i in range(n-1):
				print(i + 1, i+2)
			print(n, 1)
			a = n
			while a < m:
				print(s1, s2)
				a += 1
