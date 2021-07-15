import math
def na():
	n = int(input())
	b = [int(x) for x in input().split()]
	return n,b


def nab():
	n = int(input())
	b = [int(x) for x in input().split()]
	c = [int(x) for x in input().split()]
	return n,b,c


def dv():
	n, m = list(map(int, input().split()))
	return n,m


def dva():
	n, m = list(map(int, input().split()))
	b = [int(x) for x in input().split()]
	return n,m,b


def nm():
	n = int(input())
	b = [int(x) for x in input().split()]
	m = int(input())
	c = [int(x) for x in input().split()]
	return n,b,m,c


def dvs():
	n = int(input())
	m = int(input())
	return n, m


n,a = na()
d = {}
for i in a:
	d[i] = d.get(i, 0) + 1
ls = list(d.keys())
for i in ls:
	if d[i] > 2:
		print('NO')
		return
a1 = []
a2 = []
a = sorted(a)
for i in range(0, n - 1, 2):
	if len(a1) != 0:
		lst1 = a1[len(a1) - 1]
	else:
		lst1 = -1
	if len(a2) != 0:
		lst2 = a2[len(a2) - 1]
	else:
		lst2 = -1
	if a[i] != lst1:
		if a[i] != a[i + 1]:
			a1.append(a[i])
			a1.append(a[i + 1])
		else:
			a1.append(a[i])
			a2.append(a[i + 1])
	else:
		a1.append(a[i + 1])
		a2.append(a[i])
if n % 2 == 1:
	if a[n - 1] not in set(a1):
		a1.append(a[n-1])
	else:
		a2.append(a[n - 1])
a2 = a2[::-1]
print('YES')
print(len(a1))
if len(a1) == 0:
	print()
else:
	print(*a1)
print(len(a2))
if len(a2) == 0:
	print()
else:
	print(*a2)


