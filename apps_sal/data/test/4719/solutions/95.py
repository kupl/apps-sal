n = int(input())
res_map = dict()
s = input()
tmp_map = dict()
for j in s:
    if j not in tmp_map:
        tmp_map[j] = 1
    else:
        tmp_map[j] += 1
for j in list(tmp_map.keys()):
    res_map[j] = tmp_map[j]

for i in range(n - 1):
    s = input()
    tmp_map = dict()
    for j in s:
        if j not in tmp_map:
            tmp_map[j] = 1
        else:
            tmp_map[j] += 1
    for j in list(res_map.keys()):
        if j in tmp_map:
            res_map[j] = min(res_map[j], tmp_map[j])
        else:
            res_map[j] = 0

res = ""
for i in list(res_map.keys()):
    res += i * res_map[i]

res = sorted(res)
print(("".join(res)))
