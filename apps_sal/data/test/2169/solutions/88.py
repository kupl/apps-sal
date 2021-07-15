h, w, d = [int(x) for x in input().split()]
n = h * w

p_list = [None] * (n + 1)
for i in range(h):
    a_list = [int(x) for x in input().split()]
    for j in range(w):
        p_list[a_list[j]] = (i, j)

m_a_list = [0] * (n + 1)
for start in range(1, d + 1):
    p_i, p_j = p_list[start]
    p_target = start
    for target in range(start + d, n + 1, d):
        n_i, n_j = p_list[target]
        m = abs(n_i - p_i) + abs(n_j - p_j)
        m_a_list[target] = m + m_a_list[p_target]
        p_i, p_j, p_target = n_i, n_j, target

q = int(input())
for _ in range(q):
    l, r = [int(x) for x in input().split()]
    print(m_a_list[r] - m_a_list[l])
