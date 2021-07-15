for _ in range(int(input())):
	n, m = map(int, input().split())
	l2 = list(map(int, input().split()))
	l = sorted(l2)
	if n == 2 or m < n:
		print(-1)
		continue
	ans = 2*sum(l)
	ans += (m-n)*(l[0]+l[1])
	print(ans)
	for i in range(1, n):
		print(i, i+1)
	print(n, 1)
	for i in range(m-n):
		print(l2.index(l[0])+1, l2.index(l[1])+1)
