def main():
    _ = int(input())
    a = [int(an) for an in input().split()]
    a.sort(reverse=True)
    line = -1
    lines = []
    for an in a:
        if line == an:
            lines.append(an)
            if len(lines) == 2:
                break
            line = -1
        else:
            line = an
    print(lines[0] * lines[1] if len(lines) == 2 else 0)


def __starting_point():
    main()


__starting_point()
