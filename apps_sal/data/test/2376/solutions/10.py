(N, W) = map(int, input().split())
value_table = [[] for i in range(4)]
for i in range(N):
    (w, v) = map(int, input().split())
    if i == 0:
        w1 = w
    value_table[w - w1] += [v]
[value_table[i].sort(reverse=True) for i in range(4)]
ans = 0
value_table_ruiseki = [[0] for i in range(4)]
for i in range(4):
    for v in value_table[i]:
        value_table_ruiseki[i] += [value_table_ruiseki[i][-1] + v]
ans = 0
for (i, iv) in enumerate(value_table_ruiseki[0]):
    for (j, jv) in enumerate(value_table_ruiseki[1]):
        for (k, kv) in enumerate(value_table_ruiseki[2]):
            for (ell, ellv) in enumerate(value_table_ruiseki[3]):
                weight = i * w1 + j * (w1 + 1) + k * (w1 + 2) + ell * (w1 + 3)
                value = iv + jv + kv + ellv
                if weight <= W:
                    ans = max(ans, value)
print(ans)
