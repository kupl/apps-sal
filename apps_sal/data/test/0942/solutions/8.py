'''input
6
3 3 3 3 3 3
5
3 3 2 2 2
4
0 1 2 3


'''
n = int(input())
a = list(map(int, input().split()))
s = [0] * (n + 1)
v = [0] * (n + 1)
r = [0] * (n + 1)
b = [0] * n
m = 0
for i in range(n):
	a[i] = n - a[i]
	s[a[i]] += 1
for i in range(n):
	if r[a[i]] == 0:
		m += 1
		v[a[i]] = m
		r[a[i]] = a[i]
	b[i] = v[a[i]]
	r[a[i]] -= 1
	# print(b[i])
if any(x for x in r):
	print("Impossible")
	return
print("Possible")
print(*b)

