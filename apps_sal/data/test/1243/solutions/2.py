n = int(input())
a = list(map(int, input().split()))

k = int(sum(a)/n)
summ = 0
for i in range(n-1):
	summ += abs(a[i]-k)
	a[i+1] = a[i+1]-(k-a[i])
print(summ)
