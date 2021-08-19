n = int(input())
ts = []
res = 0
for _ in range(n):
    i = input().strip()
    m_res = 0
    s_count = 0
    for c in i:
        if c == 's':
            s_count += 1
        else:
            m_res += s_count
    res += m_res
    ts.append((i.count('s'), i.count('h')))
ts = sorted(ts, key=lambda k: float(k[0]) / float(k[1]) if k[1] else float('inf'), reverse=True)
ss = [s for (s, h) in ts]
hs2 = [h for (s, h) in ts]
hs = [0 for _ in ts]
for i in range(n - 2, -1, -1):
    hs[i] = hs2[i + 1] + hs[i + 1]
for i in range(n):
    res += ss[i] * hs[i]
print(res)
