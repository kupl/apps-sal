def main():
    s = str(input())
    b_count = s.count('B')
    w_count = len(s) - b_count

    if b_count == len(s) or w_count == len(s):
        count = 0
    else:
        count = 0
        index = 0
        alp = s[index]

        while True:
            if b_count == 0 or w_count == 0:
                break
            else:
                if s[index] == 'B':
                    b_count -= 1
                else:
                    w_count -= 1

                if s[index] == alp:
                    index += 1
                else:
                    count += 1
                    alp = s[index]
                    index += 1

        if not (b_count == 0 and w_count == 0):
            count += 1

    print(count)


def __starting_point():
    main()


__starting_point()
