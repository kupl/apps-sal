import math as m

S = list(input())
turning_point_indexes = [0]
for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        turning_point_indexes.append(i)
turning_point_indexes.append(len(S))

A = [0] * len(S)
for i in range(1, len(turning_point_indexes), 2):
    turning_point_index = turning_point_indexes[i]
    left_count = turning_point_indexes[i] - turning_point_indexes[i - 1]
    right_count = turning_point_indexes[i + 1] - turning_point_indexes[i]
    A[turning_point_index - 1] = m.ceil(left_count / 2) + m.floor(right_count / 2)
    A[turning_point_index] = m.floor(left_count / 2) + m.ceil(right_count / 2)

print(*A)
