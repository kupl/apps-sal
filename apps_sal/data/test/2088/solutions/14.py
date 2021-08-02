n = int(input())
p = list(map(int, input().split()))
gr = [[] for i in range(n)]
for i in range(n - 1):
    gr[p[i] - 1].append(i + 1)

q = [0]
after = []
i = 0
s = [0 for i in range(n)]
used = set()
used.add(0)
while q:
    cur = q.pop()
    after.append(cur)
    for el in gr[cur]:
        if el not in used:
            used.add(el)
            q.append(el)
            i += 1

q = after
for j in range(i, -1, -1):
    if len(gr[q[j]]) == 0:
        s[q[j]] = 1
    else:
        ans = 0
        for c in gr[q[j]]:
            ans += s[c]
        s[q[j]] = ans
s.sort()
print(' '.join(list(map(str, s))))
