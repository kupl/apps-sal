from collections import deque
n = int(input())
a = list(map(int, input().split()))
num_map = dict()
for i in range(n):
    if a[i] not in num_map:
        num_map[a[i]] = 1
    else:
        num_map[a[i]] += 1

keys = sorted(list(num_map.keys()), reverse=True)

q = deque()
for i in keys:
    if num_map[i] >= 2:
        q.append([i, num_map[i]])
res = 1
counter = 0
while len(q) != 0:
    key, value = q.popleft()
    res *= key
    if value - 2 >= 2:
        q.appendleft([key, value - 2])
    counter += 1
    if counter == 2:
        print(res)
        break
else:
    print((0))

