n = int(input())
A = list(map(int, input().split()))
d = {}
for a in A:
    d[a] = d.get(a, 0) + 1
comb = []
for i in d:
    if d[i] > 1:
        comb.append(d[i] * (d[i] - 1) // 2)
s = sum(comb)
keys = list(d.keys())
for a in A:
    ans = s - d[a] * (d[a] - 1) // 2 + (d[a] - 1) * (d[a] - 2) // 2
    print(ans)
