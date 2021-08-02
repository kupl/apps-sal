n = int(input())
a_l1 = list(map(int, input().split()))
a_l2 = list(map(int, input().split()))
c = 0
m_a_l1 = []
for i in a_l1:
    c += i
    m_a_l1.append(c)
c = 0
m_a_l2 = [0] * n
for i, j in enumerate(reversed(a_l2)):
    c += j
    m_a_l2[-1 - i] = c

ans = 0
for i, j in zip(m_a_l1, m_a_l2):
    ans = max(i + j, ans)
print(ans)
