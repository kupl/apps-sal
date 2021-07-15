from collections import defaultdict
m, k = (int(x) for x in input().split())
friends = defaultdict(set)
maybe = dict()
for i in range(m):
	a, b = (int(x) for x in input().split())
	friends[a].add(b)
	friends[b].add(a)
	maybe[a] = []
	maybe[b] = []
for user1 in friends:
	for user2 in friends:
		if user1 == user2:
			continue
		if user2 in friends[user1]:
			continue
		if len(friends[user1] & friends[user2]) * 100 >= k * len(friends[user1]):
			maybe[user1].append(user2)
for k, v in sorted(maybe.items()):
	print(str(k) + ':', len(v), ' '.join(str(x) for x in sorted(v)))

