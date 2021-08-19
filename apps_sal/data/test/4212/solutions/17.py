import itertools
(N, M, Q) = map(int, input().split())
seisu_list = []
for i in range(Q):
    seisu = list(map(int, input().split()))
    seisu_list.append(seisu)
M_list = [i for i in range(1, M + 1)]
A_list = list(itertools.combinations_with_replacement(M_list, N))
ans = 0
for i in range(len(A_list)):
    ans_temp = 0
    for j in range(Q):
        if A_list[i][seisu_list[j][1] - 1] - A_list[i][seisu_list[j][0] - 1] == seisu_list[j][2]:
            ans_temp += seisu_list[j][3]
            ans = max(ans, ans_temp)
print(ans)
