s = input().split()
n, t = int(s[0]), int(s[1])
a = [0 for i in range(110)]


def balance(x, d):
	if a[x] <= 1.0 or d == n:
		return
	else:
		p = (a[x] - 1.0) / 2
		a[x] = 1
		a[x+n] += p
		a[x+1] += p
		balance(x+n, d+1)
		balance(x+1, d+1)
	

a[0] += t
balance(0, 1)
	
ans = 0
for i in range(100):
	if a[i] >= 1:
		ans += 1
		
print(ans)
