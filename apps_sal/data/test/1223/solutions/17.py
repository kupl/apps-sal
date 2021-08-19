n = int(input())
p = list(map(int, input().split()))

pos_list = [0] * n
# print(index_list) [0, 0, 0, 0] n = 4 のとき
for index, i in enumerate(p, 0):
    # print(index, i)
    pos_list[i - 1] = index
    # print(index_list)

left_next_index = list(range(-1, n - 1)) + [-1, -1]
right_next_index = list(range(1, n + 1)) + [n, n]

answer = 0
# print(left_next_index)    [-1, 0, 1, -1, -1]
# print(right_next_index)   [1, 2, 3, 3, 3]
for i in range(1, n):
    index = pos_list[i - 1]
    l1 = left_next_index[index]
    l2 = left_next_index[l1]
    r1 = right_next_index[index]
    r2 = right_next_index[r1]
    # print(index, l1, l2, r1, r2, i)
    answer += i * ((index - l1) * (r2 - r1) + (r1 - index) * (l1 - l2))

    left_next_index[r1] = l1
    right_next_index[l1] = r1

print(answer)
