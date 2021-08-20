n = int(input())
us = list(map(int, input().split(' ')))
os = us[:]
os.sort()
for i in range(1, len(os)):
    os[i] += os[i - 1]
    us[i] += us[i - 1]
os = [0] + os
us = [0] + us
res = []
q = int(input())
for i in range(q):
    (t, l, r) = list(map(int, input().split(' ')))
    if t == 1:
        res.append(str(us[r] - us[l - 1]))
    else:
        res.append(str(os[r] - os[l - 1]))
print('\n'.join(res))
