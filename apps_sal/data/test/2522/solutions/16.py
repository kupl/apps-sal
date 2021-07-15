#a,b,c,d = map(int, input().split())
n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
b = b[::-1]

first = 0
last = n-1
for i in range(n):
	if a[i] == b[i]:
		if i < last and b[last] != a[i]:
			b[i],b[last] = b[last],b[i]
			last -= 1
		elif first < i and b[first] != a[i]:
			b[i],b[first] = b[first],b[i]
			first += 1

ok = True
for i in range(n):
	ok = ok and a[i] != b[i]

if ok:
	print("Yes")
	for i in range(n):
		print(b[i],end=' ')
else:
	print("No")

