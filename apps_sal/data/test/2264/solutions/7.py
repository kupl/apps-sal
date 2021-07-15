ans = []
n = int(input())

for _ in range(n):
    k = int(input())
    m_b, m_a = list(map(int, input().split()))
    for _ in range(k-1):
        a, b = list(map(int, input().split()))
        m_a = min(m_a, b)
        m_b = max(m_b, a)
    if (m_a>m_b):
        ans.append(0)
    else:
        ans.append(m_b-m_a)

for el in ans:
    print(el)

