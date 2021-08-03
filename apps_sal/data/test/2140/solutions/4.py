def __starting_point():
    s = list(input())
    input()
    data = sorted(map(lambda x: int(x) - 1, input().split()))
    data.append(len(s) // 2)

    tr = True
    for i in range(len(data) - 1):
        if tr:
            for j in range(data[i], data[i + 1]):
                s[j], s[-j - 1] = s[-j - 1], s[j]

        tr = not tr

    print(''.join(s))


__starting_point()
