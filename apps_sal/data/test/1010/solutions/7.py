n = int(input())
a = list(map(int, input().split()))
l = list([0 for i in range(n)])
j = 0
for i in range(n):
	if a[i] == 1:
		l[j] = i
		j += 1
ans = 1
if j == 0:
	print(0)
	return
for i in range(j):
	if i == 0:    
		continue
	ans *= l[i] - l[i - 1]

print(ans)
