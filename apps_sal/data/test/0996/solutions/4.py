def put():
    return map(int, input().split())


def safe(x, y, z):
    return x >= 0 and y >= 0 and z >= 0 and x < n and y < m and z < p


def check(x, y, z):
    if mat[x][y][z] == '0':
        return 0
    cur = [x, y, z]
    for i in range(3):
        src = cur.copy()
        src[i] -= 1
        if (not safe(src[0], src[1], src[2])) or mat[src[0]][src[1]][src[2]] == '0':
            continue

        for j in range(3):
            des = cur.copy()
            des[j] += 1
            alt = src.copy()
            alt[j] += 1
            if safe(des[0], des[1], des[2]) and mat[des[0]][des[1]][des[2]] == '1':
                if j == i:
                    return 1
                elif safe(alt[0], alt[1], alt[2]) and mat[alt[0]][alt[1]][alt[2]] == '0':
                    return 1
    return 0


n, m, p = put()
mat = []
ans = 0
for i in range(n):
    mat.append([input() for j in range(m)])
    if i != n - 1:
        input()

for i in range(n):
    for j in range(m):
        for k in range(p):
            ans += check(i, j, k)

print(ans)
