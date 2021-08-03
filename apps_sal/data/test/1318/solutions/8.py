import sys

# request number
n = int(sys.stdin.readline())
request = []
for i in range(1, n + 1):
    people, cost = map(int, sys.stdin.readline().split())
    request.append((i, people, cost))

#request.sort(key=lambda item: (-item[2], item[1]))
# print(request)

k = int(sys.stdin.readline())
tables = []
for tmp in zip(range(1, k + 1), [int(s) for s in sys.stdin.readline().split()]):
    tables.append(tmp)
tables.sort(key=lambda item: item[1])
# print(tables)

total = 0
ans = []
used = [False for i in range(n + 1)]
count = 0

for i, t in tables:
    max_price = 0
    request_id = -1

    for j, c, p in request:
        if p > max_price and c <= t and not used[j]:
            max_price = p
            request_id = j

    if request_id > 0:
        count += 1
        used[request_id] = True
        ans.append((request_id, i))
        total += max_price

# sorted(ans)
print(str(count) + " " + str(total))
for request_id, i in ans:
    print(str(request_id) + " " + str(i))
