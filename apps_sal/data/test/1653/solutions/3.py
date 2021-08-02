def main():
    s, t = input(), input()
    s_info, t_info = fast_counter(s), fast_counter(t)

    queries = int(input())
    answer = ''
    for _ in range(queries):
        l1, r1, l2, r2 = list(map(int, input().split()))
        l1, l2 = l1 - 1, l2 - 1

        from_mask = mask(l1, r1, s_info)
        to_mask = mask(l2, r2, t_info)

        if can_transform(from_mask, to_mask):
            answer += '1'
        else:
            answer += '0'

    print(answer)


def can_transform(from_mask, to_mask):
    if from_mask[0] > to_mask[0]:
        return False
    elif (to_mask[0] - from_mask[0]) % 2 != 0:
        return False
    elif to_mask[0] == from_mask[0]:
        if to_mask[1] > from_mask[1]:
            return False
        return (from_mask[1] - to_mask[1]) % 3 == 0
    elif from_mask[0] == 0:
        return to_mask[1] < from_mask[1]
    else:
        return to_mask[1] <= from_mask[1]


def mask(l, r, info):
    return (info[1][r] - info[1][l], min(r - l, info[0][r]))


def fast_counter(s):
    a_last, b_count = [0], [0]
    for c in s:
        if c == 'A':
            a_last.append(a_last[-1] + 1)
            b_count.append(b_count[-1])
        else:
            a_last.append(0)
            b_count.append(b_count[-1] + 1)
    return (a_last, b_count)


main()
