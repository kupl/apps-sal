n = int(input())
count = 0
for i in range(n):
	line = [int(j) for j in input().split()]
	if line[1] - line[0] > 1:
		count += 1
print(count)
