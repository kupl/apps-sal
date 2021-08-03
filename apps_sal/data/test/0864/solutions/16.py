from collections import defaultdict

n, m = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
food = [0 for i in range(101)]
users = [0 for i in range(101)]

for i in x:
    food[i] += 1
days = 1000
for i in range(n):
    best = 0
    cand = -1
    for j in range(101):
        if (food[j] // (users[j] + 1)) > best:
            best = food[j] // (users[j] + 1)
            cand = j
    users[cand] += 1
    days = min(days, best)

print(days)
