def read_nums():
    return [int(x) for x in input().split()]


def parse_input(text, symbols='?*'):
    res = []
    prev_index = 0
    for index, char in enumerate(text):
        if char in symbols:
            res.append(('', text[prev_index: index - 1]))
            res.append((char, text[index - 1]))
            prev_index = index + 1
    last_chunk = text[prev_index:]
    if len(last_chunk) != 0:
        res.append(('', last_chunk))
    return res


def calc_length(parsed_input):
    res = 0
    for part in parsed_input:
        if part[0] == '':
            res += len(part[1])
    return res


def main():
    msg = input()
    n, = read_nums()
    parsed_input = parse_input(msg)
    length = calc_length(parsed_input)

    out = []
    for part in parsed_input:
        if part[0] == '':
            out.append(part[1])
        elif length < n:
            if part[0] == '?':
                out.append(part[1])
                length += 1
            else:
                out.append(part[1] * (n - length))
                length = n

    res = ''.join(out)
    if len(res) == n:
        print(res)
    else:
        print('Impossible')


def __starting_point():
    main()


__starting_point()
