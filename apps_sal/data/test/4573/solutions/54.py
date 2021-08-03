n = int(input())
x = list(map(int, input().split()))
x_2 = sorted(x)
m_1 = x_2[n // 2 - 1]
m_2 = x_2[n // 2]
for i in range(n):
    if x[i] <= m_1:
        print(m_2)
    elif x[i] >= m_2:
        print(m_1)
