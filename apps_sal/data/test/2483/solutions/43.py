(n, c) = list(map(int, input().split()))
program = [[] for _ in range(c)]
for i in range(n):
    (s, t, cc) = list(map(int, input().split()))
    program[cc - 1].append((s, t))
count = [0] * (10 ** 5 + 1)
for i in range(c):
    program[i].sort()
    l = len(program[i])
    judge = True
    for j in range(l - 1):
        if judge:
            count[program[i][j][0] - 1] += 1
        if program[i][j][1] == program[i][j + 1][0]:
            judge = False
        else:
            judge = True
        if judge:
            count[program[i][j][1]] -= 1
    if l == 0:
        continue
    if judge:
        count[program[i][l - 1][0] - 1] += 1
    count[program[i][l - 1][1]] -= 1
ans = 0
for i in range(10 ** 5 + 1):
    if i != 0:
        count[i] += count[i - 1]
    if ans < count[i]:
        ans = count[i]
print(ans)
