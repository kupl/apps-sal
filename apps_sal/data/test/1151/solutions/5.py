import sys

string = sys.stdin.readline()
n = int(string.split()[0])
u = int(string.split()[1])
levels = tuple(map(int, sys.stdin.readline().split()))
if len(levels) < 3:
    sys.stdout.write('-1')
    return

i, j, k = 0, 1, 2
indices = (0, 1, 2)
level_i = levels[0]
level_j = levels[1]
nu = levels[2] - level_i
nu = -1
while i < n - 2:
    while k < n - 1 and levels[k + 1] - level_i <= u:
        k += 1
    nu_cur = levels[k] - level_i
    if nu_cur <= u:
        nu_cur = (levels[k] - level_j) * 1 / nu_cur
    else:
        nu_cur = -1
    if nu_cur > nu:
        nu = nu_cur
        indices = (i, j, k)
    i += 1
    j += 1
    k = max(k, j + 1)
    level_j = levels[j]
    level_i = levels[i]

sys.stdout.write(str(nu))
