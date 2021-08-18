N, K, Q = list(map(int, input().split()))
A_list = []
for _ in range(Q):
    A_list.append(int(input()))

A_cor_list = [0] * N

for a in A_list:
    A_cor_list[a - 1] += 1

for a_cur in A_cor_list:
    if K - (Q - a_cur) > 0:
        print("Yes")
    else:
        print("No")
