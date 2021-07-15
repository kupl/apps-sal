n = int(input())
a = [int(x)-1 for x in input().split()]
count = [0 for i in range(len(a))]
ans = [-1 for i in range(len(a))]
for i in range(len(a)):
	if a[i] < len(count):
		count[a[i]] += 1

for i in range(len(a)):
	if a[i] < len(count):
		if count[a[i]] >= 1:
			ans[i] = a[i]
			count[a[i]] = -1

jIt = 0
for i in range(len(ans)):
	if ans[i] == -1:
		while count[jIt] < 0:
			jIt += 1
		ans[i] = jIt
		jIt += 1

print(" ".join(str(x+1) for x in ans))
