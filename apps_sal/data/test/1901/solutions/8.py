
from collections import deque

class Person:
    def __init__(self):
        self.friends = []
        self.taken = False
        self.price = 0

def fill(person):
    queue = deque([])
    queue.append(person)
    minimum = person.price

    while queue:
        p = queue.popleft()
        p.taken = True
        minimum = min(minimum, p.price)
        for f in p.friends:
            if not f.taken:
                queue.append(f)
    return minimum


N, M = map(int, input().split())

people = [Person() for _ in range(0, N)]

prices = list(map(int, input().split()))
for i in range(0, N):
    people[i].price = prices[i]

for _ in range(0, M):
    u, v = map(int, input().split())
    people[u-1].friends.append(people[v-1])
    people[v-1].friends.append(people[u-1])

cost = 0
for p in people:
    if not p.taken:
        cost += fill(p)

print(cost)
