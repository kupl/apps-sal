n = int(input())
a = list(map(int, input().split()))

a = [n-x for x in a]

groups = {}
for i, x in enumerate(a):
	if x not in groups:
		groups[x] = []
	groups[x].append(i)

hats = [0] * n
current_hat = 1

for count, ids in list(groups.items()):
	if len(ids)%count != 0:
		print("Impossible")
		return

	for g in range(len(ids)//count):
		for _id in ids[count*g:count*(g+1)]:
			hats[_id] = current_hat
		current_hat += 1

print("Possible")
print(*hats)

