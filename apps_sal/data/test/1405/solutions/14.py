n = int(input())
a = list(map(int,input().split()))
ans = a.count(0)
d = {}
for i in a:
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1

ans = max(ans, 2)

for i in range(n):
	for j in range(n):
		
		if(i != j and (a[i] != 0 or a[j] != 0)):

			first = a[i]
			second = a[j]
			temp = [first, second]
			third = first + second

			while(True):

				if abs(third) > int(1e9):
					break

				if third not in d:
					break

				temp.append(third)

				first = second
				second = third
				third = first + second

			count = 0
			f = 1
			for k in range(len(temp)):
				if d[temp[k]] > 0:
					d[temp[k]] -= 1
					count += 1
				else:
					f = 0
					for j in range(k):
						d[temp[j]] += 1
					break
			if f:
				for k in temp:
					d[k] += 1
			ans = max(ans, count)


print(ans)

