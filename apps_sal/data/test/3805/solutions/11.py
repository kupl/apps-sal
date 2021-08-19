def main():
    stack = []
    for c in input():
        if stack and c == stack[-1]:
            del stack[-1]
        else:
            stack.append(c)
    print(('Yes', 'No')[bool(stack)])


def __starting_point():
    main()


__starting_point()
