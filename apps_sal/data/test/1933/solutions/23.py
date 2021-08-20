(n, m, k) = [int(i) for i in input().split()]
a = []
for i in range(n):
    b = [int(i) for i in input().split()]
    a.append(b)
b = [0] * m
for i in range(k + 2):
    a.append(b)
score = 0
repl = 0
for j in range(m):
    cur_sum = 0
    cur_max = 0
    cur_best_repl = 0
    cur_repl = 0
    for i in range(k):
        cur_sum += a[i][j]
    for i in range(n):
        if a[i][j] == 0:
            cur_sum += a[i + k][j]
            continue
        if cur_max < cur_sum:
            cur_max = cur_sum
            cur_best_repl = cur_repl
        cur_sum = cur_sum - 1 + a[i + k][j]
        cur_repl += 1
    score += cur_max
    repl += cur_best_repl
print(score, repl)
