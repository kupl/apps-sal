n = int(input())
ans = []
while n > 3:
	ans.append(2)
	n -= 2
ans.append(n)
print(len(ans))
for i in ans:
	print(i, end=" ")

