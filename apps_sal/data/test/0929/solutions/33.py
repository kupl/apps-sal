H, W = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(H)]
# print(a)
q = []
for i in range(H):
    if i % 2 == 0:
        for j in range(W):
            q.append([i, j])
    elif i % 2 == 1:
        for j in range(W - 1, -1, -1):
            q.append([i, j])
# print(q)
N = 0
ans_arr = []
for qi in range(len(q)):
    i = q[qi][0]
    j = q[qi][1]
    if a[i][j] % 2 == 0:
        pass
    elif a[i][j] % 2 == 1 and qi != len(q) - 1:
        N += 1
        a[i][j] -= 1
        a[q[qi + 1][0]][q[qi + 1][1]] += 1
        ans_arr.append([i, j, q[qi + 1][0], q[qi + 1][1]])

print(N)
for x1, x2, x3, x4 in ans_arr:
    print((x1 + 1, x2 + 1, x3 + 1, x4 + 1))

