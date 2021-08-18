from heapq import heappop, heappush
n, k = map(int, input().split())
s = []
h = set()
l = [0] * n
for _ in range(n):
    t, d = map(int, input().split())
    s.append((d, t - 1))
s = sorted(s, reverse=True)
a = []
num = 0
for i in range(k):
    d, t = s[i]
    l[t] += 1
    h.add(t)
    num += d
    if l[t] > 1:
        heappush(a, (d, t))
ans = len(h)**2 + num
for j in range(k, n):
    d, t = s[j]
    l[t] += 1
    if l[t] >= 2:
        continue
    if len(a) == 0:
        break
    d1, t1 = heappop(a)
    h.add(t)
    num = num - d1 + d
    ans = max(ans, len(h)**2 + num)
print(ans)
