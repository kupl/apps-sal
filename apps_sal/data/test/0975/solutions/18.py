n = int(input())
sherlock = [int(i) for i in list(input())]
moriarty = [int(i) for i in list(input())]

pairs = []
for i in range(n):
    for j in range(n):
        pairs.append((moriarty[j] - sherlock[i], i, j))

pairs = sorted(pairs)

sherlock_marked = [False] * n
moriarty_marked = [False] * n

avoided = 0

for pair in pairs:
    if pair[0] < 0:
        continue

    if not sherlock_marked[pair[1]] and not moriarty_marked[pair[2]]:
        sherlock_marked[pair[1]] = True
        moriarty_marked[pair[2]] = True
        avoided += 1

sherlock_marked = [False] * n
moriarty_marked = [False] * n

flicked = 0

for pair in pairs:
    if pair[0] < 1:
        continue

    if not sherlock_marked[pair[1]] and not moriarty_marked[pair[2]]:
        sherlock_marked[pair[1]] = True
        moriarty_marked[pair[2]] = True
        flicked += 1

print(n - avoided)
print(flicked)
