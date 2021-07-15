import math
import sys
input = sys.stdin.readline


# def solve_rec(R, moves):
#     all_good = True
#     # print('solve_rec', R, moves)
#     for i in range(1, len(R)):
#         for j in range(1, len(R[0])):
#             if not R[i][j]:
#                 all_good = False
#                 break

#     if all_good:
#         return moves

#     if moves >= 3:
#         return math.inf

#     answer = math.inf
#     for i in range(len(R)-1):
#         for j in range(len(R)-1):
#             R2 = copy.deepcopy(R)
#             R2[i][j] = not R2[i][j]
#             R2[i+1][j] = not R2[i+1][j]
#             R2[i][j+1] = not R2[i][j+1]
#             R2[i+1][j+1] = not R2[i+1][j+1]
#             answer = min(answer, solve_rec(R2, moves+1))
#     return answer


n, m = [int(_) for _ in input().split()]
M = []
for i in range(n):
    row = input()[:-1]
    M.append(row)

if n >= 4 and m >= 4:
    print(-1)
elif n == 1 or m == 1:
    print(0)
else:
    if n <= m:
        R = [[True] * (m-1) for _ in range(2)]
        for i in range(n-1):
            for j in range(m-1):
                count = 0
                if M[i][j] == '1':
                    count += 1
                if M[i+1][j+1] == '1':
                    count += 1
                if M[i+1][j] == '1':
                    count += 1
                if M[i][j+1] == '1':
                    count += 1
                if not (count % 2):
                    R[i][j] = False
    else:
        R = [[True] * (n-1) for _ in range(2)]
        for i in range(m-1):
            for j in range(n-1):
                count = 0
                if M[j][i] == '1':
                    count += 1
                if M[j+1][i+1] == '1':
                    count += 1
                if M[j+1][i] == '1':
                    count += 1
                if M[j][i+1] == '1':
                    count += 1
                if not (count % 2):
                    R[i][j] = False

    mnm = max(n, m)
    dp_all_good = [math.inf] * (mnm)
    dp_all_bad = [math.inf] * (mnm)
    dp_top_bad = [math.inf] * (mnm)
    dp_bot_bad = [math.inf] * (mnm)

    dp_all_good[0] = 0
    dp_all_bad[0] = 0
    dp_top_bad[0] = 0
    dp_bot_bad[0] = 0

    for i in range(1, len(R[0])+1):
        if R[0][i-1] and R[1][i-1]:
            dp_all_good[i] = min(dp_all_good[i], dp_all_good[i-1])
            dp_all_bad[i] = min(dp_all_bad[i], dp_all_bad[i-1]+1)
            dp_top_bad[i] = min(dp_top_bad[i], dp_top_bad[i-1]+1)
            dp_bot_bad[i] = min(dp_bot_bad[i], dp_bot_bad[i-1]+1)
        if (not R[0][i-1]) and (not R[1][i-1]):
            dp_all_good[i] = min(dp_all_good[i], dp_all_bad[i-1]+1)
            dp_all_bad[i] = min(dp_all_bad[i], dp_all_good[i-1])
            dp_top_bad[i] = min(dp_top_bad[i], dp_bot_bad[i-1]+1)
            dp_bot_bad[i] = min(dp_bot_bad[i], dp_top_bad[i-1]+1)
        if R[0][i-1] and (not R[1][i-1]):
            dp_all_good[i] = min(dp_all_good[i], dp_bot_bad[i-1]+1)
            dp_all_bad[i] = min(dp_all_bad[i], dp_top_bad[i-1]+1)
            dp_top_bad[i] = min(dp_top_bad[i], dp_all_bad[i-1]+1)
            dp_bot_bad[i] = min(dp_bot_bad[i], dp_all_good[i-1])
        if (not R[0][i-1]) and R[1][i-1]:
            dp_all_good[i] = min(dp_all_good[i], dp_top_bad[i-1]+1)
            dp_all_bad[i] = min(dp_all_bad[i], dp_bot_bad[i-1]+1)
            dp_top_bad[i] = min(dp_top_bad[i], dp_all_good[i-1])
            dp_bot_bad[i] = min(dp_bot_bad[i], dp_all_bad[i-1]+1)

    # print(R)
    # print(dp_all_good)
    # print(dp_all_bad)
    # print(dp_top_bad)
    # print(dp_bot_bad)

    print(min(dp_all_good[mnm-1], dp_all_bad[mnm-1]+1, dp_bot_bad[mnm-1]+1, dp_top_bad[mnm-1]+1))

