num_problems = int(input())
t = [int(n) for n in input().split()]
total = sum(t)
num_drinks = int(input())

for i in range(num_drinks):
    m_id, m_val = [int(n) for n in input().split()]
    ans = total - t[m_id - 1] + m_val
    print(ans)
