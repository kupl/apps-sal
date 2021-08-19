n = int(input())
table = []
for i in range(2 * n - 1):
    li = list(map(int, input().split()))
    for j in range(i + 1):
        table.append([li[j], i + 2, j + 1])
table.sort(key=lambda x: x[0], reverse=True)
res = [0 for _ in range(2 * n)]
entry = 0
idx = 0
while entry != n:
    t = table[idx]
    (t1, t2) = (t[1] - 1, t[2] - 1)
    if res[t1] == 0 and res[t2] == 0:
        res[t1] = t2 + 1
        res[t2] = t1 + 1
        entry += 1
    idx += 1
print(' '.join(map(str, res)))
