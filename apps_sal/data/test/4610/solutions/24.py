(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
num_map = dict()
for i in range(n):
    if a[i] not in num_map:
        num_map[a[i]] = 1
    else:
        num_map[a[i]] += 1
rest_key_num = max(0, len(num_map) - k)
values = sorted(list(num_map.values()))
res = 0
for j in range(rest_key_num):
    res += values[j]
print(res)
