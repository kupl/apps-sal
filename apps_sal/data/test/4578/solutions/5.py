
N, X = map(int, input().split())
min_req = 0
for i in range(N):
    m = int(input())
    min_req += m
    if i == 0:
        m_min = m
    else:
        if m_min > m:
            m_min = m

num = N + ((X - min_req) // m_min)
print(num)
