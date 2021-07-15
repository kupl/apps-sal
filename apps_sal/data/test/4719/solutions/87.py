from collections import Counter
n = int(input())

D = Counter(list(input()))
for i in range(n-1):
    d = Counter(list(input()))
    key = D.keys()
    for k in key:
        D[k] = min(D[k], d[k])

ans = []
key = D.keys()
for k in key:
    for i in range(D[k]):
        ans.append(k)
ans.sort()
print("".join(ans))
