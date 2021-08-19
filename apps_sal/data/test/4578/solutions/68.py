(N, X) = map(int, input().split())
m_list = [int(input()) for i in range(N)]
donatu = 0
sum_m_list = sum(m_list)
X_nokori = X - sum_m_list
donatu += N
donatu = donatu + X_nokori // min(m_list)
print(donatu)
