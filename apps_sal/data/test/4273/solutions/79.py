from collections import defaultdict
N = int(input())
defdict = defaultdict(int)
for _ in range(N):
    st = input()
    fst = st[0]
    if fst in 'MARCH':
        defdict[fst] += 1
V = list(defdict.values())
NV = len(V)
ans = 0
for i in range(NV):
    for j in range(i + 1, NV):
        for k in range(j + 1, NV):
            ans += V[i] * V[j] * V[k]
print(ans)
