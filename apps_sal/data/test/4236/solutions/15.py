n, m = list(map(int, input().split()))
all = set(range(1, m + 1))
for i in range(n):
	l, r = list(map(int, input().split()))
	for j in range(l, r + 1):
		all.discard(j)

print(len(all))
print(*all)

