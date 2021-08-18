from itertools import *
maxans = 0
poss = []


def getsum(perm):
    nonlocal maxans, poss
    ans = 0
    n = len(perm)
    h = [0] * n
    for i in range(n):
        for j in range(i, n):
            ans += min(perm[i:j + 1])
#            for k in range(i, j + 1):
#                h[k] += 1
    if ans > maxans:
        maxans = ans
        poss = [perm]
    elif ans == maxans:
        poss.append(perm)
    return ans


n, m = list(map(int, input().split()))
lst = list(range(1, n + 1))
perms = list(permutations(lst))
for i in range(len(perms)):
    getsum(perms[i])
# print(maxans)
print(' '.join(map(str, poss[m - 1])))
