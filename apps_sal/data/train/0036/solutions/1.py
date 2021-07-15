n, p, m, w = int(input()), list(map(int, input().split())), int(input()), sorted(enumerate(map(int, input().split())), key = lambda x: x[1])
ans, pos = [-1] * m, [0, 0]
for i, c in w:
    while pos[0] + p[pos[1]] < c:
        pos[0] += p[pos[1]]
        pos[1] += 1
    ans[i] = pos[1] + 1
print(*ans, sep = '\n')

