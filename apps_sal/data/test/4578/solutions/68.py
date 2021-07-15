N, X = map(int, input().split())
m_list = [int(input()) for i in range(N)]

donatu = 0

# とりあえずm_listの合計をXから引く
sum_m_list = sum(m_list)
X_nokori = X - sum_m_list
donatu += N

# その後m_listの最小値と残ったXで割り算
donatu = donatu + X_nokori // min(m_list)

print(donatu)
