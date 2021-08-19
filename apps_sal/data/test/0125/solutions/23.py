# left, strait, right, pedastrian
#   3
# 4     2
#   1
def check_if_safe(curr_part, left_part, right_part, opposite_part):
    curr_left, curr_straight, curr_right, curr_pedastrian = curr_part
    if curr_pedastrian == 0:
        return True
    elif (curr_left + curr_right + curr_straight) > 0:
        return False
    left_left, left_straight, left_right, left_pedastrian = left_part
    if left_right == 1:
        return False
    right_left, right_straight, right_right, right_pedastrian = right_part
    if right_left == 1:
        return False
    opposite_left, opposite_straight, opposite_right, opposite_pedastrian = opposite_part
    if opposite_straight == 1:
        return False
    return True


part_one = [int(x) for x in input().split()]
part_two = [int(x) for x in input().split()]
part_three = [int(x) for x in input().split()]
part_four = [int(x) for x in input().split()]

ans = (check_if_safe(part_one, part_four, part_two, part_three)
      + check_if_safe(part_two, part_one, part_three, part_four)
      + check_if_safe(part_three, part_two, part_four, part_one)
       + check_if_safe(part_four, part_three, part_one, part_two)
       )
if ans != 4:
    print('YES')
else:
    print('NO')
