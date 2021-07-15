n = int(input())
a = input().split()
s = 0
i = 0
for i in range(n - 2):
	if a[i] == '1' and a[i + 1] == '0' and a[i + 2] == '1':
		a[i + 2] = '0'
		s += 1
print(s)
