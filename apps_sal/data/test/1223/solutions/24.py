N = int(input())
P_id = [0] * (N + 1)  # P_id[i]は順列Pに置けるiのindex, P[0]は無視
for index, p in enumerate(map(int, input().split())):
    P_id[p] = index

left_next_index = list(range(- 1, N - 1)) + ['うんこ', - 1]  # + [- 1]ではないことに注意, left_next_index[r1] = l1においてr1 = Nの場合があるから
right_next_index = list(range(1, N + 1)) + [N, 'うんこ']

res = 0
for p in range(1, N):
    l1 = left_next_index[P_id[p]]
    l2 = left_next_index[l1]
    r1 = right_next_index[P_id[p]]
    r2 = right_next_index[r1]

    res += p * ((l1 - l2) * (r1 - P_id[p]) + (P_id[p] - l1) * (r2 - r1))

    left_next_index[r1] = l1
    right_next_index[l1] = r1

print(res)
