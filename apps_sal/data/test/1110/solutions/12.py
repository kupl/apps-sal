n = int(input())
sum = 0
for x in range(1,n) :
	sum += (n - x) * x
sum += n
print(sum)

