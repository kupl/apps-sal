from collections import defaultdict

dist = list(map(int, input().split()))

a = [0] * 11

indexes = {'S':0, 'M':1, 'L':2, 'XL':3, 'XXL':4, 'XXXL':5, 'S,M':6, 'M,L':7, 'L,XL':8, 'XL,XXL':9, 'XXL,XXXL':10}
inv = dict(list(zip(list(indexes.values()), list(indexes.keys()))))

n = int(input())

par_d = defaultdict(list)

par = [None] * n

for i in range(n):
    ind = indexes[input().strip()]

    if ind <= 5:
        dist[ind] -= 1
        par[i] = ind
    else:
        par_d[ind].append(i)

    a[ind] += 1

if min(dist) < 0:
    print("NO")
    return

k = 0
k_p = []

for i in range(6, 11):
    size = i - 6

    dist[size] -= k
    if dist[size] < 0:
        print("NO")
        return
    else:
        for j in k_p:
            par[j] = size

    m = len(par_d[i])

    if dist[size] + dist[size+1] < m:
        print("NO")
        return

    if dist[size] <= m:
        p = par_d[i][:dist[size]]
        k_p = par_d[i][dist[size]:]

        k = m - dist[size]
        for j in p:
            par[j] = size
        dist[size] = 0

    else:
        p = par_d[i]
        k_p = []

        k = 0
        for j in p:
            par[j] = size

if k > dist[-1]:
    print("NO")
    return

else:
    for j in k_p:
        par[j] = 5


print('YES')
for i in range(n):
    print(inv[par[i]])

