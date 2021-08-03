n = int(input())
a = list(map(int, input().split()))
num_map = dict()
for i in range(n):
    if a[i] not in num_map:
        num_map[a[i]] = 1
    else:
        num_map[a[i]] += 1

res = 0
for key, value in list(num_map.items()):
    if key <= value:
        res += value - key
    else:
        res += value

print(res)
