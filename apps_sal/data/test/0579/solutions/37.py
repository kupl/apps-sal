(N, K) = map(int, input().split())
P_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))
checked_list = [0 for _ in range(N)]
min_INF = -1 * 10 ** 10
max_score = min_INF
for i in range(N):
    if checked_list[i] == 1:
        continue
    posit = i
    loop_list = [posit]
    score_list = []
    for j in range(N):
        posit = P_list[posit] - 1
        if j == 0:
            score_list.append(C_list[posit])
        else:
            score_list.append(score_list[-1] + C_list[posit])
        if posit in loop_list:
            break
        loop_list.append(posit)
    len_loop = len(loop_list)
    max_score_list = max(score_list)
    around_score = score_list[-1]
    temp_score_base = 0
    if around_score > 0 and K // len_loop > 0:
        temp_score_base += (K // len_loop - 1) * around_score
    for k in range(len_loop):
        checked_list[loop_list[k]] = 1
        temp_max_score = temp_score_base
        rest_score = min_INF
        if around_score > 0 and K // len_loop > 0:
            rest_score = max(max_score_list, max(score_list[:K % len_loop], default=min_INF) + around_score)
        rest_score = max(max(score_list[:min(K, len_loop)]), rest_score)
        temp_max_score = temp_max_score + rest_score
        max_score = max(max_score, temp_max_score)
        now_score = score_list.pop(0)
        len_score = len(score_list)
        score_list = [score_list[l] - now_score for l in range(len_score)]
        score_list.append(score_list[-1] + now_score)
print(max_score)
