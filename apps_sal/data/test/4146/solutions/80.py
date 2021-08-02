n = int(input())
v = list(input().split())
v0 = {}
v1 = {}
for i in range(0, n, 2):
    if v[i] in v0:
        v0[v[i]] += 1
    else:
        v0[v[i]] = 1
for i in range(1, n, 2):
    if v[i] in v1:
        v1[v[i]] += 1
    else:
        v1[v[i]] = 1
v0 = sorted(v0.items(), key=lambda x: x[1], reverse=True)
v1 = sorted(v1.items(), key=lambda x: x[1], reverse=True)
if v0[0][0] == v1[0][0]:
    if len(v0) == 1:
        print(int(n / 2))
    else:
        print(n - v0[0][1] - (v0[1][1] if v0[1][1] > v1[1][1] else v1[1][1]))
else:
    print(n - v0[0][1] - v1[0][1])
