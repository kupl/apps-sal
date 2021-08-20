from copy import deepcopy
(h, w, k) = map(int, input().split())
s = [list(map(int, input().strip())) for i in range(h)]
ss = deepcopy(s)
for i in range(h):
    for j in range(w - 1):
        ss[i][j + 1] += ss[i][j]


def gru_hol(HOL):
    groups_a = []
    group_a = [0]
    for i in range(h - 1):
        if HOL[i] == 1:
            groups_a.append(group_a)
            group_a = [i + 1]
        else:
            group_a.append(i + 1)
    groups_a.append(group_a)
    return groups_a


def nex_hol(HOL):
    for j in range(h - 1):
        if HOL[j] == 0:
            HOL[j] = 1
            for k in range(0, j):
                HOL[k] = 0
            break
    return HOL


def cutsum(grp, lscut, nxcut):
    count = 0
    for i in grp:
        if lscut != 0:
            count = count + ss[i][nxcut - 1] - ss[i][lscut - 1]
        else:
            count += ss[i][nxcut - 1]
    return count


def cutcheck(grp_a, lscut_a):
    ct_a = 0
    for i in grp_a:
        ct_a += s[i][lscut_a]
    if ct_a > k:
        return False
    else:
        return True


min_cut = h + w - 2
hol = [0] * (h - 1)
for i in range(2 ** (h - 1)):
    fl_ag = 0
    lastcut = 0
    cuts = 0
    groups = gru_hol(hol)
    for j in range(1, w):
        flag = 0
        for group in groups:
            if cutsum(group, lastcut, j + 1) > k:
                if cutcheck(group, lastcut) == False:
                    fl_ag = 1
                    break
                else:
                    flag = 1
        if fl_ag == 1:
            break
        if flag == 1:
            cuts += 1
            lastcut = j
    if cutcheck(group, w - 1) == True:
        min_cut = min(min_cut, cuts + sum(hol))
    nex_hol(hol)
print(min_cut)
