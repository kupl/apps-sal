length, k = map(int, input().split())

problems = list(enumerate(map(int, input().split(' '))))

problems.sort(key=lambda i: i[1], reverse=True)

maxs = problems[:k]

maxs.sort()

distr = []

prev = -1
total = 0
for i in range(k):
    distr.append(maxs[i][0] - prev)
    prev = maxs[i][0]
    total += distr[-1]

distr[-1] += length - total

print(sum(map(lambda i: i[1], maxs)))
print(*distr)
