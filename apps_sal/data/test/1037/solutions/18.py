import pprint
N = int(input())
A = list(map(int, input().split()))


def student_sorting(N, A):
    student_list = [0] * N
    for (initial_pos, activity) in enumerate(A):
        student_list[initial_pos] = (activity, initial_pos)
    return sorted(student_list, reverse=True)


def DP(N, student_list):
    DP_map = list((list((0 for row in range(N + 1 - column))) for column in range(N + 1)))
    ans_list = []
    ans = 0
    for left in range(N):
        activity = student_list[left][0]
        distance_l = abs(left - student_list[left][1])
        DP_map[left + 1][0] = DP_map[left][0] + activity * distance_l
    for right in range(N):
        activity = student_list[right][0]
        distance_r = abs(N - 1 - right - student_list[right][1])
        DP_map[0][right + 1] = DP_map[0][right] + activity * distance_r
    for left in range(1, N + 1):
        for right in range(1, N - left + 1):
            activity = student_list[left + right - 1][0]
            distance_l = abs(left - 1 - student_list[left + right - 1][1])
            distance_r = abs(N - right - student_list[left + right - 1][1])
            score_if_appended_to_left = DP_map[left - 1][right] + activity * distance_l
            score_if_appended_to_right = DP_map[left][right - 1] + activity * distance_r
            DP_map[left][right] = max(score_if_appended_to_left, score_if_appended_to_right)
    for left in range(N + 1):
        row = N - left
        column = left
        ans_list.append(DP_map[column][row])
    ans = max(ans_list)
    return ans


student_list = student_sorting(N, A)
ans = DP(N, student_list)
print(ans)
