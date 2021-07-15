n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(len(l)):
	for j in range(i+1, len(l)):
		for k in range(j+1, len(l)):
			if (l[i] != l[j] and l[j] != l[k] and l[i] != l[k] and l[i]+l[j] > l[k] and l[j]+l[k] > l[i] and l[k]+l[i] > l[j]):
				ans += 1
print(ans)
