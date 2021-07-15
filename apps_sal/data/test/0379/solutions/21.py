n, m = list(map(int, input().split()))
puzz = []
for _ in range(n):
    puzz.append([1 if x == 'X' else 0 for x in input()])
hor, ver = set(), set()
for i, l in enumerate(puzz):
    for j, quad in enumerate(l):
        if quad:
            hor.add(i)
            ver.add(j)
ans = True
for i in hor:
    for j in ver:
        if not puzz[i][j]:
            ans = False
            break
print('YES' if ans else 'NO')

