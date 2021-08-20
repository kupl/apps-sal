n = int(input())
data = {}
for i in range(n):
    s = str(input())
    if s in data.keys():
        data[s] += 1
    else:
        data[s] = 1
m = max(list(data.values()))
ans = []
for (j, k) in data.items():
    if k == m:
        ans.append(j)
for l in sorted(ans):
    print(l)
