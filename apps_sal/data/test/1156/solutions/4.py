n = int(input())
a = list(map(int, input().split()))
b = list(map(lambda x: 1 if x == '1' else 0, input()))
left, right = - 10 ** 9, 10 ** 9
for i in range(4, n):
	test = True
	for j in range(2, 5):
		if b[i - j] != b[i - 1]:
			test = False
	if not test:
		continue
	if b[i] == 0 and b[i - 1] == 1:
		for j in range(5):
			right = min(right, a[i - j] - 1)
	if b[i] == 1 and b[i - 1] == 0:
		for j in range(5):
			left = max(left, a[i - j] + 1)
print(left, right)
