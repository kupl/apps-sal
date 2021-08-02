def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
c = list(map(int, input().split()))
k = list(map(int, input().split()))
st = []
ed = []
ans = 0
is_st = [1] * n
parent = [-1] * n
d = {i: c[i] for i in range(n)}
for i in range(n):
    m = min(d, key=d.get)
    if(is_st[m]):
        st.append(m)
    else:
        ed.append([m, parent[m]])
    ans = ans + d[m]
    del d[m]
    for j in d.keys():
        t_cost = (k[m] + k[j]) * dist(p[m], p[j])
        if(t_cost < d[j]):
            d[j] = t_cost
            parent[j] = m
            is_st[j] = 0
print(ans)
print(len(st))
for i in st:
    print(i + 1, end=" ")
print()
print(len(ed))
for i in ed:
    print(i[0] + 1, i[1] + 1)
