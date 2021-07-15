def main():
    stack = []
    for c in input():
        if stack and stack[-1] != c:
            del stack[-1]
        else:
            stack.append(c)
    print(''.join(reversed(stack)))


def __starting_point():
    main()

__starting_point()
