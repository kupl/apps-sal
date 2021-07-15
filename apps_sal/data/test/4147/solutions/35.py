N, A, B, C = list(map(int, input().split()))
L_list = [int(input()) for i in range(N)]

import itertools

Target = itertools.product([0, 1, 2, 3], repeat=N)

INF = 10 ** 9
#Target = [(1,2,2,2,3)]
ans = INF
for T in Target:
    A_sum = 0
    B_sum = 0
    C_sum = 0
    A_cost = 0
    B_cost = 0
    C_cost = 0
    for i in range(N):
        if T[i] == 0: continue
        if T[i] == 1:
            if A_sum == 0:
                A_sum += L_list[i]
            else:
                A_sum += L_list[i]
                A_cost += 10
        if T[i] == 2:
            if B_sum == 0:
                B_sum += L_list[i]
            else:
                B_sum += L_list[i]
                B_cost += 10
        if T[i] == 3:
            if C_sum == 0:
                C_sum += L_list[i]
            else:
                C_sum += L_list[i]
                C_cost += 10

    if min(A_sum, B_sum, C_sum) == 0: continue

    ans = min(ans, abs(A - A_sum)+A_cost + abs(B - B_sum)+B_cost + abs(C - C_sum)+C_cost)
print(ans)

