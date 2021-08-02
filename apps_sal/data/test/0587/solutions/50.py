N, K, *L = map(int, open(0).read().split())
ls = []
for i, (t, d) in enumerate(zip(*[iter(L)] * 2)):
    ls.append((d, t))
ls.sort()
S = set()
pre = []
ans = 0
num = 0
for i in range(K):
    d, t = ls.pop()
    ans += d
    if t not in S:
        num += 1
        S.add(t)
    else:
        pre.append(d)
pre.sort(reverse=True)
ans += num * num
if pre == []:
    print(ans)
    return
m = ans
for i in range(N - K):
    d, t = ls.pop()
    if t in S:
        continue
    S.add(t)
    m -= pre.pop()
    m += d + 2 * num + 1
    num += 1
    ans = max(ans, m)
    if pre == []:
        break
print(ans)
