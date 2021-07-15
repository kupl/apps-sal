from collections import Counter

n = int(input())
lang = Counter(list(map(int, input().split())))

m = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = list()

for i in range(m):
	res.append((lang[a[i]], lang[b[i]], i))

print(sorted(sorted(res, key = lambda x: x[1], reverse = True), key = lambda x: x[0], reverse = True)[0][2] + 1)
