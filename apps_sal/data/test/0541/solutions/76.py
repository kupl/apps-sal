N, M = map(int, input().split())
table = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    table.append((a, b))
table = sorted(table, key=lambda x: x[1])
cur_r = table[0][1]
ans = 1
for i in range(1, M):
    l, r = table[i]
    if cur_r <= l:
        ans += 1
        cur_r = r

print(ans)
