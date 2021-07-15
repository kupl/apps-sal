n, m, k = [int(i) for i in input().split()]
values = []
for i in range(m):
	values.append(int(input()))
count = 0
p = int(input())
for value in values:
	if bin(p ^ value).count('1') <= k:
		count += 1
print(count)


