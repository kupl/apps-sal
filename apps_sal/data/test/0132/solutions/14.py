#python3
#utf-8

pieces_nr = int(input())
piece_idx___deg = [int(x) for x in input().split()]
ans = 360
for left_cl in range(pieces_nr):
    for right_op in range(left_cl + 1, pieces_nr + 1):
        curr_split = sum(piece_idx___deg[left_cl:right_op])
        rest = 360 - curr_split
        # print(curr_split, rest)
        curr_ans = rest - curr_split
        if curr_ans < 0:
            curr_ans *= -1
        ans = min(curr_ans, ans)
        # print(curr_ans)
print(ans)

