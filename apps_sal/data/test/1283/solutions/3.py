n, k = list(map(int, input().split()))
field = [input() for i in range(n)]
field_ = [''.join([field[i][j] for i in range(n)]) for j in range(n)]

for_ans = [[0] * n for i in range(n)]
for_s = '.' * k

for i, el in enumerate(field):
    for j in range(n - k + 1):
        if el[j: j + k] == for_s:
            for j_ in range(j, j + k):
                for_ans[i][j_] += 1

for i, el in enumerate(field_):
    for j in range(n - k + 1):
        if el[j: j + k] == for_s:
            for j_ in range(j, j + k):
                for_ans[j_][i] += 1

ans = 0
x, y = 1, 1

for i in range(n):
    for j in range(n):
        if for_ans[i][j] > ans:
            ans = for_ans[i][j]
            x = i + 1
            y = j + 1

print(x, y)
