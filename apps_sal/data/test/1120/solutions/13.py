n = int(input())

count = 0
while n:
	n -= max(list(map(int,str(n))))
	count += 1

print(count)
