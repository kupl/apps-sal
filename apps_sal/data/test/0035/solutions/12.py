n, m = map(int, input().split())

f = [0 for _ in range(n)]

for i in range(n):
    f[i] = input()


hor = True

if n % 3 != 0:
    hor = False
else:
    c = "RGB"
    used = {"R": False, "G": False, "B": False}
    used[f[0][0]] = True

    cnt = 0
    if [f[0][0] * m for i in range(n // 3)] == \
       f[:n // 3]:
        cnt += 1

    if not used[f[n // 3][0]]:
        used[f[n // 3][0]] = True
        if [f[n // 3][0] * m for i in range(n // 3)] == \
           f[n // 3: n // 3 * 2]:
            cnt += 1

    if not used[f[n // 3 * 2][0]]:
        used[f[n // 3 * 2][0]] = True
        if [f[n // 3 * 2][0] * m for i in range(n // 3)] == \
           f[n // 3 * 2:]:
            cnt += 1

    if cnt == 3:
        hor = True
    else:
        hor = False

ver = True

if m % 3 != 0:
    ver = False
else:
    new_f = ["" for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_f[i] += f[j][i]

    c = "RGB"
    used = {"R": False, "G": False, "B": False}
    used[new_f[0][0]] = True

    cnt = 0
    if [new_f[0][0] * n for i in range(m // 3)] == \
       new_f[:m // 3]:
        cnt += 1

    if not used[new_f[m // 3][0]]:
        used[new_f[m // 3][0]] = True
        if [new_f[m // 3][0] * n for i in range(m // 3)] == \
           new_f[m // 3: m // 3 * 2]:
            cnt += 1

    if not used[new_f[m // 3 * 2][0]]:
        used[new_f[m // 3 * 2][0]] = True
        if [new_f[m // 3 * 2][0] * n for i in range(m // 3)] == \
           new_f[m // 3 * 2:]:
            cnt += 1

    if cnt == 3:
        ver = True
    else:
        ver = False

if hor or ver:
    print("YES")
else:
    print("NO")
