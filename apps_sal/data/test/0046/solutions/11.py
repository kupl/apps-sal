n, m = list(map(int, input().split()))
n_rem = [n // 5 for _ in range(5)]
for i in range(1, n % 5 + 1):
    n_rem[i] += 1
m_rem = [m // 5 for _ in range(5)]
for i in range(1, m % 5 + 1):
    m_rem[i] += 1
print(sum([n_rem[i] * m_rem[(5 - i) % 5] for i in range(5)]))
