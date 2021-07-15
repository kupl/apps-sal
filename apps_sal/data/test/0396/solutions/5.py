l, r = list(map(int, input().split()))
x = 31
y = 20
count = 0
for i in range(x + 1):
	for j in range(y + 1):
		if 2 ** i * 3 ** j >= l and 2 ** i * (3 ** j) <= r:
			count += 1
print(count)			

