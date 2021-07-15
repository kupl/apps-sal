n, m = list(map(int, input().split()))
l_d, l_h = list(map(int, input().split()))
m_h = l_h + l_d - 1
for i in range(1, m):
    n_d, n_h = list(map(int, input().split()))
    if abs(n_h - l_h) > n_d - l_d:
        print("IMPOSSIBLE")
        return
    m_h = max(m_h, max(l_h, n_h) + (n_d - l_d - abs(n_h - l_h)) // 2)
    l_d, l_h = n_d, n_h
m_h = max(m_h, l_h + n - l_d)
print(m_h)

