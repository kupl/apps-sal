def read_list():
    return list(map(int, input().strip().split(' ')))


def print_list(l):
    print(' '.join(map(str, l)))


(n, p) = read_list()
a = read_list()
a.sort()
mi = max((a[i] - i for i in range(n)))
res = []
ll = []
x = mi
now = x
i = 0
dic = [[-1]]
for step in range(n):
    while i < n and now >= a[i]:
        i += 1
    now += 1
    tmp = (i - step) % p
    tmp = (p - tmp) % p
    if step >= tmp:
        dic.append([tmp, step])
dic.pop(0)
for i in range(len(dic) - 1, 0, -1):
    if dic[i][0] <= dic[i - 1][1] - 1:
        dic[i - 1][1] = dic[i][1]
        dic[i - 1][0] = min(dic[i][0], dic[i - 1][0])
        dic.pop(i)
las = 0
for d in dic:
    flag = True
    for i in range(las, d[0]):
        if i >= p - 1:
            flag = False
            break
        res.append(mi + i)
    las = d[1] + 1
    if not flag:
        break
if dic:
    for i in range(dic[-1][-1] + 1, p - 1):
        res.append(mi + i)
print(len(res))
print_list(res)
