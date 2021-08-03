n, m = [int(x) for x in input().split()]
n_rem = [n // 5] * 5
m_rem = [m // 5] * 5
for i in range(n % 5):
    n_rem[(i + 1) % 5] += 1
for i in range(m % 5):
    m_rem[(i + 1) % 5] += 1
print((n_rem[0] * m_rem[0] + n_rem[1] * m_rem[4] +
      n_rem[2]*m_rem[3] + n_rem[3]*m_rem[2] + n_rem[4]*m_rem[1]))
