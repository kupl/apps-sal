def main():
    n = int(input())
    S = input()
    fl = 0
    for i in range(len(S) - 3):
        if S[i] == '.':
            continue
        else:
            for j in range(1, len(S) // 4 + 1):
                for k in range(5):
                    if i + k * j >= len(S) or S[i + k * j] == '.':
                        break
                else:
                    fl = 1
                    break
        if fl:
            break
    if fl:
        print('yes')
    else:
        print('no')


def __starting_point():
    main()


__starting_point()
