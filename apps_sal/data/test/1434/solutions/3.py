n = int(input())
v = []
deg1 = []
degsum = 0
has_v = [True] * n
for i in range(n):
    (d, s) = list(map(int, input().split()))
    degsum += d
    if d == 1:
        deg1.append(i)
    if d == 0:
        has_v[i] = False
    v.append([d, s])
edge = []
while deg1 != []:
    f = deg1[0]
    del deg1[0]
    if has_v[f] is False:
        continue
    v[f][0] -= 1
    has_v[f] = False
    t = v[f][1]
    edge.append([f, t])
    v[t][0] -= 1
    v[t][1] ^= f
    if v[t][0] == 1:
        deg1.append(t)
    elif v[t][0] == 0:
        has_v[t] = False
print(degsum // 2)
for (f, t) in edge:
    print(f, t)
