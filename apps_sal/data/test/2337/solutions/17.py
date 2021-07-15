n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
ptr = 0
found = 0
for task in a:
	while ptr < m and b[ptr] < task:
		ptr += 1
	if ptr < m and b[ptr] >= task:
		found += 1
		ptr += 1
print(n - found)

