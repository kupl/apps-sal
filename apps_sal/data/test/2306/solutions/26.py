n = int(input())
t = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]
time = sum(t)

speed = [10 ** 9] * (2 * time + 1)
limit = [10 ** 9] * (2 * time + 1)

i = 0
for j, k in zip(t, v):
    for _ in range(j * 2):
        limit[i] = min(limit[i], k)
        i += 1
    limit[i] = min(limit[i], k)

s = 0
for i in range(2 * time + 1):
    s = min(s, limit[i])
    speed[i] = min(speed[i], s)
    s += 0.5
s = 0
for i in reversed(list(range(2 * time + 1))):
    s = min(s, limit[i])
    speed[i] = min(speed[i], s)
    s += 0.5

dist = 0
for i in range(2 * time):
    dist += (speed[i] + speed[i + 1]) / 4
print(dist)

