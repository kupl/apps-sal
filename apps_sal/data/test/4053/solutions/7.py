n = int(input())
all = [input() for _ in range(2 * n - 2)]
imp = []
ans = [0 for _ in range(2 * n - 2)]
pr = []
for a in all:
    if len(a) == n - 1:
        imp.append(a)

ok = True
for i in range(2 * n - 2):
    is1, is2 = False, False
    if imp[0].find(all[i]) == 0:
        is1 = True
    if imp[1].rfind(all[i]) == len(imp[1]) - len(all[i]):
        is2 = True

    if not is1 and not is2:
        ok = False
        continue

    if is1 and is2:
        if all[i] in pr:
            is1 = False
        else:
            is2 = False

    if is1:
        ans[i] = 1
        pr.append(all[i])
    else:
        ans[i] = 2

if not ok:
    imp[0], imp[1] = imp[1], imp[0]
    ans = [0 for _ in range(2 * n - 2)]
    pr = []

    for i in range(2 * n - 2):
        is1, is2 = False, False
        if imp[0].find(all[i]) == 0:
            is1 = True
        if imp[1].rfind(all[i]) == len(imp[1]) - len(all[i]):
            is2 = True

        if is1 and is2:
            if all[i] in pr:
                is1 = False
            else:
                is2 = False

        if is1:
            ans[i] = 1
            pr.append(all[i])
        else:
            ans[i] = 2

for i in range(2 * n - 2):
    if ans[i] == 1:
        print('P', end='')
    else:
        print('S', end='')
print()
