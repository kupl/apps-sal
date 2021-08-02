import collections
N = int(input())
S = []
ans = []
for i in range(N):
    S.append(input())
d = collections.Counter(S)
ome = max(d.values())
for k, v in list(d.items()):
    if v == ome:
        ans.append(k)
ans.sort()
for x in ans:
    print(x)
