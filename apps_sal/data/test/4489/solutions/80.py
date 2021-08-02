from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
ans = 0
sc = list(set(s.copy()))
sn = Counter(s)
tn = Counter(t)
for i in range(len(sc)):
    ans = max(sn[sc[i]] - tn[sc[i]], ans)
print(ans)
