(n, m) = map(int, input().split(' '))
matrix = []
for i in range(n):
    matrix.append(input())
m_value = []
for i in range(m):
    for j in range(n):
        if matrix[j][i] == '*':
            m_value.append(n - j)
            break
max_up = 0
max_down = 0
for i in range(1, m):
    if m_value[i] - m_value[i - 1] > max_up:
        max_up = m_value[i] - m_value[i - 1]
    if m_value[i] - m_value[i - 1] < max_down:
        max_down = m_value[i] - m_value[i - 1]
print(max_up, -max_down)
