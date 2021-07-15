from itertools import accumulate

MAX = 200002

n, k, q = list(map(int, input().split()))

info = [0] * MAX
for i in range(n):
    l, r = list(map(int, input().split()))
    info[l] += 1
    info[r + 1] -= 1

acc = 0
for ind, diff in enumerate(info):
    acc += diff
    if acc >= k:
        info[ind] = 1
    else:
        info[ind] = 0

pref = list(accumulate(info))
ans = []
for i in range(q):
    l, r = list(map(int, input().split()))
    ans.append(str(pref[r] - pref[l - 1]))

print('\n'.join(ans))

