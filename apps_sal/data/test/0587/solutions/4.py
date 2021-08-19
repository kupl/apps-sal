(n, k) = map(int, input().split())
td = [list(map(int, input().split()))[::-1] for _ in range(n)]
td.sort(reverse=1)
s = set()
ss = set()
a = []
b = []
c = []
for i in range(n):
    if i < k:
        (d, t) = td[i]
        if t in s:
            b.append(d)
        else:
            a.append(d)
            s.add(t)
            ss.add(t)
    else:
        (d, t) = td[i]
        if t not in ss:
            c.append(d)
            ss.add(t)
c = c[::-1]
ls = len(s)
su = sum(a) + sum(b)
ans = ls * ls + su
for i in range(min(len(b), len(c))):
    ls += 1
    su -= b.pop()
    su += c.pop()
    ans = max(ans, ls * ls + su)
print(ans)
