n, m, s, t = list(map(int , input().split()))
dors = []
for i in range(n+1):
    dors.append(set()) # инициализируем множество смежных вершин

for i in range(m):
    a, b = list(map(int , input().split()))
    dors[a].add(b)
    dors[b].add(a)

dists = [-1] *(n+1)   # расстояния от старта
dists[s] = 0
q = [s]
v = 0
while v < len(q):
    cur = q[v]
    for nextv  in dors[cur]:
        if dists[nextv] < 0:
            dists[nextv] = dists[cur] +1
            q.append(nextv)
    v += 1



distt = [-1] *(n+1) # расстояния от финиша
distt[t] = 0
q = [t]
v = 0
while v < len(q):
    cur = q[v]
    for nextv  in dors[cur]:
        if distt[nextv] < 0:
            distt[nextv] = distt[cur] +1
            q.append(nextv)
    v += 1



reqdist = dists[t] - dists [s] -1

res  =0

# print(dists)
# print(distt)

for v in range(1, n+1):
    for j in range(v+1, n+1):
        if  (j in dors[v]):
            continue
        if dists[v] + distt[j] >= reqdist and dists[j] + distt[v] >= reqdist:
            res +=1
            # print(v,j, 'can be added')


print(res)

# print(rset)

