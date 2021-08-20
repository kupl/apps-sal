def get_sum(side):
    result = 0
    for i in range(len(side)):
        result += side[i][0] * side[i][1]
    return result


def main():
    left = []
    right = []
    s = input()
    middle_pos = s.index('^')
    for i in range(len(s)):
        if s[i] == '=' or s[i] == '^':
            continue
        if i < middle_pos:
            left.append((int(s[i]), abs(middle_pos - i)))
        else:
            right.append((int(s[i]), abs(middle_pos - i)))
    left_sum = get_sum(left)
    right_sum = get_sum(right)
    if left_sum > right_sum:
        print('left')
    elif right_sum > left_sum:
        print('right')
    else:
        print('balance')


def __starting_point():
    main()


__starting_point()
