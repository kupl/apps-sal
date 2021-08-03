def safe(pos):
    return pos[0] >= 0 and pos[0] < n and pos[1] >= 0 and pos[1] < m and pos[2] >= 0 and pos[2] < p


def CPU_status(pos, number):
    return safe(pos) and super_computer[pos[0]][pos[1]][pos[2]] == number


def critical(x, y, z):
    if super_computer[x][y][z] != '0':
        current = [x, y, z]
        for i in range(3):
            parent = current.copy()
            parent[i] -= 1
            if CPU_status(parent, '1'):
                for j in range(3):
                    child, alt = current.copy(), parent.copy()
                    child[j] += 1
                    alt[j] += 1
                    if CPU_status(child, '1') and (CPU_status(alt, '0') or j == i):
                        return 1
    return 0


n, m, p = map(int, input().split())
super_computer, crit = ([], 0)
for i in range(n):
    super_computer.append([input() for _ in range(m)])
    if i != n - 1:
        input()
for i in range(n):
    for j in range(m):
        for k in range(p):
            crit += critical(i, j, k)
print(crit)
