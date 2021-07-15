n, L, R = list(map(int, input().strip().split()))

if n < 2 :
	ans = n % 2
else :
	a = []
	while n != 0 :
		a.append(n)
		n = n // 2

	pw2 = []
	pw2.append(1)
	for i in range(1, 51) :
		pw2.append(pw2[i-1] * 2)

	ans = 0
	for i in range(L, R + 1) :
		if i % 2 == 1 :
			ans += 1
		else :
			cnt = 0
			while i % pw2[cnt] == 0 :
				cnt += 1
			ans += a[len(a) - cnt] % 2
print(ans)
