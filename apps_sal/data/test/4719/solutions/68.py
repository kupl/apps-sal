from collections import Counter
n = int(input())
X = input()
preC = Counter(X)
preS = set(X)
for _ in range(n - 1):
    X = input()
    C = Counter(X)
    preS = set(X) & preS
    d = {}
    for s in preS:
        d[s] = min(C[s], preC[s])
    preC = d
ans = []
for s in preS:
    for _ in range(preC[s]):
        ans.append(s)
print(''.join(sorted(ans)))
