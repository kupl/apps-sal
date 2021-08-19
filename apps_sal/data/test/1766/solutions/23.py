# -------------------------------------------------------------------------------
# Name:        Ð Â Ð’Â Ð â€™Ð’Â Ð Â Ð Ð‹Ð â€™Ð’Â˜Ð Â Ð’Â Ð â€™Ð’Â Ð Â Ð Ð‹Ð Ð†Ð â€šÐ¡Ñ›Ð Â Ð’Â Ð â€™Ð’Â Ð Â Ð¡Ñ›Ð Ð†Ð â€šÐ’Â˜Ð Â Ð’Â Ð Â Ð â€¹Ð Â Ð Ð‹Ð Ð†Ð â€šÐ¡Ñ™Ð Â Ð’Â Ð â€™Ð’Â Ð Â Ð²Ð‚â„¢Ð â€™Ð’Â»Ð Â Ð’Â Ð Â Ð â€¹Ð Â Ð’Â Ð Â Ð²Ð‚Â°1
# Purpose:
#
# Author:      Anatoliy
#
# Created:     30.09.2013
# Copyright:   (c) Anatoliy 2013
# Licence:     <your licence>
# -------------------------------------------------------------------------------

def main():
    number_of_elements = int(input())
    s = input()
    s_list = s.split(" ")
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
    print(str(sereja) + " " + str(dima))


def __starting_point():
    main()


__starting_point()
