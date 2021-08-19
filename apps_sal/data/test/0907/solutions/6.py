(n, m) = list(map(int, input().split()))
ms = []
cnt = {}


def cd(x):
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1


for i in range(m):
    (x, y) = list(map(int, input().split()))
    ms.append((x, y))
    cd(x)
    cd(y)
ans = []
for (k, v) in list(cnt.items()):
    if v >= m // 2:
        ans.append(k)


def check_one(c):
    for i in range(m):
        (x, y) = ms[i]
        if x == c or y == c:
            continue
        if check_two(c, x, i):
            return True
        if check_two(c, y, i):
            return True
        return False
    return True


def check_two(c1, c2, s):
    for i in range(s, m):
        (x, y) = ms[i]
        if x == c1 or x == c2 or y == c1 or (y == c2):
            continue
        else:
            return False
    return True


for a in ans:
    if check_one(a):
        print('YES')
        quit()
print('NO')
