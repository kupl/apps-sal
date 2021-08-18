

letters = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])


def check(s, i):
    tested_s = str(i)
    used_letters, used_digits = dict(), dict()
    for ch, tested_ch in zip(s, tested_s):
        if ch == '?':
            continue
        if ch in letters:
            if ch in used_letters:
                if used_letters[ch] != tested_ch:
                    return False
            elif tested_ch in used_digits:
                if used_digits[tested_ch] != ch:
                    return False
            else:
                used_letters[ch] = tested_ch
                used_digits[tested_ch] = ch
            continue
        if ch != tested_ch:
            return False
    return True


def __starting_point():
    s = input()
    count = 0

    for i in range(10 ** (len(s) - 1), (10 ** (len(s)))):
        if check(s, i):
            count += 1

    print(count)


__starting_point()
