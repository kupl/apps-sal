def main():
    n = input()
    letters = list(input().split(' '))
    idx = list()
    for i in range(len(letters)):
        if letters[i] == '1':
            idx.append(i)
    m = len(idx)
    if m == 0:
        print(0)
        return
    res = 1
    for i in range(1, m):
        res += min(2, idx[i] - idx[i - 1])
    print(res)


def __starting_point():
    main()


__starting_point()
