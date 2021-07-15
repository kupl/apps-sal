n, x = map(int, input().split())
m_list = []

for i in range(n):
  m = int(input())
  m_list.append(m)

mod = x - sum(m_list)
ans = mod // min(m_list)
print(ans + len(m_list))
