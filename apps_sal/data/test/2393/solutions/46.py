def check_string(string):
    indexes = get_matches(string)
    length = len(indexes)
    print(length)
    print(' '.join(indexes))


def get_matches(string):
    indexes = []
    for index in range(0, len(string) - 2):
        check_fragment = string[index:index + 3]
        is_one = check_fragment == 'one'
        if is_one:
            one_start = string[index - 2:index]
            if one_start != 'tw':
                indexes.append(str(index + 2))
        else:
            is_two = check_fragment == 'two'
            if is_two:
                check_fragment = string[index:index + 5]
                is_twone = check_fragment == 'twone'
                if is_twone:
                    indexes.append(str(index + 3))
                else:
                    indexes.append(str(index + 2))
    return indexes


for i in range(int(input())):
    c = input()
    check_string(c)
