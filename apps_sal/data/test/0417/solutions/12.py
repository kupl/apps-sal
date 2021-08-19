import numpy as np
(N, X, D) = map(int, input().split())
if not D:
    if not X:
        print(1)
    else:
        print(N + 1)
else:
    num_dict = dict()
    ans = 0
    for i in range(N + 1):
        left_num = int(i * X / D) + int(i * (i - 1) / 2)
        right_num = int(i * X / D) + int(i * (2 * N - 1 - i) / 2)
        judge_num = i * X % D
        if not judge_num in num_dict:
            num_dict[judge_num] = [(left_num, right_num)]
        else:
            num_dict[judge_num].append((left_num, right_num))
    for (j, k) in num_dict.items():
        new_k = sorted(k)
        L = new_k[0][0]
        R = new_k[0][1]
        for l in new_k:
            if l[0] <= R <= l[1]:
                R = l[1]
            elif R < l[0] and R < l[1]:
                ans += R - L + 1
                (L, R) = (l[0], l[1])
        ans += R - L + 1
    print(ans)
