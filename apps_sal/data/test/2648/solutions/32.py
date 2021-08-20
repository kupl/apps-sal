n = int(input())
a = list(map(int, input().split()))
num_map = dict()
for i in range(n):
    if a[i] not in num_map:
        num_map[a[i]] = 1
    else:
        num_map[a[i]] += 1
counter = 0
for (key, value) in list(num_map.items()):
    if value % 2 == 0:
        num_map[key] = 2
        counter += 1
    else:
        num_map[key] = 1
res = len(num_map) - counter % 2
print(res)
