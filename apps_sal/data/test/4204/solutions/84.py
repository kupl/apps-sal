def number_count(string, n):
    count = 0
    for i in range(len(string)):
        if int(string[i]) == n:
            count += 1
    return count


def main():
    s = str(input())
    k = int(input())

    if number_count(s, 1) == len(s):   # sの中身がすべて１の場合
        number = '1'

    else:
        for i in range(len(s)):
            if s[i] != '1':
                first_index = i
                break

        if k < first_index + 1:
            number = '1'
        else:
            number = s[first_index]

    print(number)


def __starting_point():
    main()


__starting_point()
