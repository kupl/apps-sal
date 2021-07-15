a, k = input().split()
k = int(k)
a = list(a)
n = len(a)
for i in range(n):
	ptr = i
	for j in range(i, i + min(k + 1, n - i)):
		if a[j] > a[ptr]:
			ptr = j
	a = a[:i] + [a[ptr]] + a[i:ptr] + a[ptr + 1:]
	k -= ptr - i
print(''.join(a))

