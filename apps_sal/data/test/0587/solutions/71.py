(n, k) = list(map(int, input().split()))
s = set()
l = []
ln = [[] for i in range(n)]
for i in range(n):
    (t, m) = list(map(int, input().split()))
    l.append([m, t - 1])
    ln[t - 1].append(m)
l.sort(reverse=True)
cand = []
ans = 0
mod = []
for i in range(k):
    ans += l[i][0]
    if l[i][1] in s:
        mod.append(l[i][0])
    else:
        s.add(l[i][1])
x = len(s)
now = ans + x ** 2
for i in range(n):
    if i in s or ln[i] == []:
        continue
    cand.append(max(ln[i]))
cand.sort(reverse=True)
for i in range(min(len(mod), len(cand))):
    ans += cand[i] - mod[-1 - i]
    x += 1
    now = max(now, ans + x ** 2)
print(now)
