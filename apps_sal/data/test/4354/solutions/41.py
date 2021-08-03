n, m = map(int, input().split())
students = [list(map(int, input().split())) for i in range(n)]

targets = [list(map(int, input().split())) for i in range(m)]
x = 0
snumber = [(0, x)] * n


def md(s, t):
    d = abs(s[0] - t[0]) + abs(s[1] - t[1])
    return d


for i in range(n):
    x = 4 * 10 ** 8
    for j in range(m):
        if x > md(students[i], targets[j]):
            x = md(students[i], targets[j])
            snumber[i] = (j + 1, md(students[i], targets[j]))

for i in range(n):
    print(snumber[i][0])
