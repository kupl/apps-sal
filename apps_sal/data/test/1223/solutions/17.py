n = int(input())
p = list(map(int, input().split()))

pos_list = [0] * n
for index, i in enumerate(p, 0):
    pos_list[i - 1] = index

left_next_index = list(range(-1, n - 1)) + [-1, -1]
right_next_index = list(range(1, n + 1)) + [n, n]

answer = 0
for i in range(1, n):
    index = pos_list[i - 1]
    l1 = left_next_index[index]
    l2 = left_next_index[l1]
    r1 = right_next_index[index]
    r2 = right_next_index[r1]
    answer += i * ((index - l1) * (r2 - r1) + (r1 - index) * (l1 - l2))

    left_next_index[r1] = l1
    right_next_index[l1] = r1

print(answer)
