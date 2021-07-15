ans = []
def fillin1(m, n, r1, r2, r3, r4):
	if m > 2*n:
		temp = m - 2*n + 2
		if temp < 4:
			if temp == 3:
				ans.extend([r2, r1, r4])
			elif temp == 2:
				ans.extend([r1, r4])
			fillin1(m-temp, n-1, r1+2, r2+2, r3+2, r4+2)
		
		else:
			ans.extend([r2, r1, r3, r4])
			fillin1(m-4, n-1, r1+2, r2+2, r3+2, r4+2)
	else:
		ans.extend(list(range(r1, r1+m)))

n, m = map(int, input().split(' '))
fillin1(m, n, 1, n*2+1, n*2+2, 2)
ans = map(lambda x: str(x), ans)
print(' '.join(ans))
