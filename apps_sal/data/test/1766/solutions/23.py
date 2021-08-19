def main():
    number_of_elements = int(input())
    s = input()
    s_list = s.split(' ')
    for i in range(0, number_of_elements):
        s_list[i] = int(s_list[i])
    sereja = 0
    dima = 0
    for i in range(0, int(number_of_elements / 2)):
        if s_list[0] > s_list[-1]:
            sereja = sereja + s_list.pop(0)
        else:
            sereja = sereja + s_list.pop(-1)
        if s_list[0] > s_list[-1]:
            dima = dima + s_list.pop(0)
        else:
            dima = dima + s_list.pop(-1)
    sereja = sereja + sum(s_list)
    print(str(sereja) + ' ' + str(dima))


def __starting_point():
    main()


__starting_point()
