from operator import *
n = int(input())
company = []
g_max = 0
dic = {}
for i in range(n):
    t = list(map(int, input().split()))
    company.append(t)
    g_max = max(g_max, max(t[1:]))
for i in range(n):
    dic[i] = company[i][0] * (g_max - max(company[i][1:]))
itr = sorted(list(dic.items()), key=itemgetter(1))
res = 0
for i in itr:
    if i[1] != 0:
        res += i[1]
print(res)
