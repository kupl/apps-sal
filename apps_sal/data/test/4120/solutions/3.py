from math import inf
nmk = list(map(int, input().split(' ')))
n = nmk[0]
m = nmk[1]
k = nmk[2]
a = []
for i in range(m):
    a.append(list(map(int, input().split(' '))))
smej = [[] for j in range(n)]
nums = {}
t = 0
for i in a:
    nums.update({(i[0], i[1]): t})
    t += 1
    smej[i[0] - 1].append(i[1] - 1)
    smej[i[1] - 1].append(i[0] - 1)
dists = [inf for i in range(n)]
dists[0] = 0
q = [0]
while len(q) > 0:
    u = q.pop(0)
    for i in smej[u]:
        if dists[i] == inf:
            q.append(i)
            dists[i] = dists[u] + 1
p = [[] for i in range(n)]
for i in range(1, n):
    for j in smej[i]:
        if dists[j] == dists[i] - 1:
            try:
                p[i].append(nums[j + 1, i + 1])
            except:
                p[i].append(nums[i + 1, j + 1])
am = 1
p.pop(0)
for i in range(len(p)):
    am *= len(p[i])
if am < k:
    print(am)
else:
    print(k)
f = [0 for i in range(len(p))]
ans = []
for i in range(k):
    s = ['0' for i in range(m)]
    for j in range(len(p)):
        s[p[j][f[j]]] = '1'
    s = ''.join(s)
    ans.append(s)
    ok = False
    first = True
    for j in range(len(p) - 1, -1, -1):
        if first:
            first = False
            if f[j] + 1 == len(p[j]):
                if j == 0:
                    ok = True
                    break
                f[j] = 0
                f[j - 1] += 1
            else:
                f[j] += 1
                break
        elif f[j] == len(p[j]):
            if j == 0:
                ok = True
                break
            else:
                f[j] = 0
                f[j - 1] += 1
    if ok:
        break
for j in range(len(ans)):
    print(ans[j])
