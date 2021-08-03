from sys import stdin

lines, line_index = stdin.readlines(), -1


def get_line():
    nonlocal lines, line_index

    line_index += 1
    return lines[line_index]


def main():
    string = get_line().strip()

    stack = []

    for c in string:
        if not stack:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if not stack:
        print('Yes')
    else:
        print('No')


main()
