n = int(input())
p_l = list(map(int, input().split()))
m_p_l = []
min_p = float('inf')
for i, p in enumerate(p_l):
    min_p = min(min_p, p)
    m_p_l.append(min_p)
ans = 0
for i, p in enumerate(p_l):
    if p == m_p_l[i]:
        ans += 1
print(ans)
