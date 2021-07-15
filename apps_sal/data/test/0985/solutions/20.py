from math import factorial
T = int(input())
a = {}
b = {}
for i in range(T):
	n, m = list(map(int, input().split(' ')))
	if n-m in a:
		a[n-m] += 1
	elif n-m not in a:
		a[n-m] = 1

	if n+m in b:
		b[n+m] += 1
	elif m+n not in b:
		b[n+m] = 1

ans = 0
for i in a:
	if a[i]>1:
		ans += factorial(a[i])//(2*factorial(a[i]-2))

for i in b:
	if b[i]>1:
		ans += factorial(b[i])//(2*factorial(b[i]-2))
print(ans)
