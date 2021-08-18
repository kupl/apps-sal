jump_r = {}
jump_l = {}


def bracket_to_value(bracket):
    if bracket == '(':
        return 1
    if bracket == ')':
        return -1


def move_r(c):
    if c + 1 in jump_r:
        return jump_r[c + 1] + 1
    else:
        return c + 1


def move_l(c):
    if c - 1 in jump_l:
        return jump_l[c - 1] - 1
    else:
        return c - 1


def remove_bracket(s, c, length):

    val = bracket_to_value(s[c])
    initial_c = c
    dir = bracket_to_value(s[c])
    if dir == 1:
        c = move_r(c)
    if dir == -1:
        c = move_l(c)
    val += bracket_to_value(s[c])
    while val != 0:
        if dir == 1:
            c = move_r(c)
        if dir == -1:
            c = move_l(c)
        val += bracket_to_value(s[c])
    final_c = c

    left_end = min(initial_c, final_c)
    right_end = max(initial_c, final_c)
    real_r_end = right_end
    real_l_end = left_end
    jump_r[left_end] = right_end
    jump_l[right_end] = left_end
    if right_end + 1 in jump_r:
        real_r_end = jump_r[right_end + 1]
    if left_end - 1 in jump_l:
        real_l_end = jump_l[left_end - 1]

    jump_l[real_r_end] = real_l_end
    jump_r[real_l_end] = real_r_end

    if real_r_end < length - 1:
        new_c = real_r_end + 1
    else:
        new_c = real_l_end - 1

    return new_c


def smart_print(s):
    i = 0
    while i < n:
        if i not in jump_r:
            print(s[i], end='')
            i += 1
        else:
            i = jump_r[i] + 1


def perform_order(order, s, c, length):
    if order == 'R':
        return move_r(c)
    if order == 'L':
        return move_l(c)
    if order == 'D':
        return remove_bracket(s, c, length)


n, m, p = [int(x) for x in input().split()]
p = p - 1
se = input()
orders = input()
for ord in orders:
    p = perform_order(ord, se, p, n)

smart_print(se)
