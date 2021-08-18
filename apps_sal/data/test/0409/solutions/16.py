def is_ab(prev, current):
    return prev == 'A' and current == 'B'


def is_ba(prev, current):
    return prev == 'B' and current == 'A'


def is_matched(prev, current):
    return is_ab(prev, current) or is_ba(prev, current)


def main():
    s = input()
    i = 0
    total_ab = 0
    total_ba = 0
    total_confused = 0

    current_len = 0

    prev = ''

    while i < len(s):
        current = s[i]
        if current_len != 0:
            if is_matched(prev, current):
                current_len += 1
            else:
                if current_len == 2:
                    if is_ab(s[i - 2], s[i - 1]):
                        total_ab += 1
                    elif is_ba(s[i - 2], s[i - 1]):
                        total_ba += 1
                elif current_len == 3:
                    total_confused += 1
                elif current_len == 4:
                    total_confused += 1
                elif current_len > 4:
                    total_confused += 2
                if current == 'A' or current == 'B':
                    current_len = 1
                else:
                    current_len = 0
        elif current == 'A' or current == 'B':
            current_len = 1

        prev = current
        i += 1

    if len(s) >= 2 and current_len >= 2:
        current = s[len(s) - 1]
        prev = s[len(s) - 2]
        if current_len == 2:
            if is_ab(prev, current):
                total_ab += 1
            elif is_ba(prev, current):
                total_ba += 1
        elif current_len == 3:
            total_confused += 1
        elif current_len == 4:
            total_confused += 1
        elif current_len > 4:
            total_confused += 2

    if total_ba >= 1 and total_ab >= 1:
        print('YES')
    elif total_confused >= 2:
        print('YES')
    elif (total_ab >= 1 or total_ba >= 1) and total_confused >= 1:
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
