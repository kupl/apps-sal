def possible_change(l):
    twenty_fives = 0
    fivties = 0

    for currency in l:
        if currency == 25:
            twenty_fives += 1
        elif currency == 50:
            if twenty_fives >= 1:
                twenty_fives -= 1
                fivties += 1
            else:
                return "NO"

        elif currency == 100:
            if twenty_fives >= 1 and fivties >= 1:
                fivties -= 1
                twenty_fives -= 1

            elif twenty_fives >= 3:
                twenty_fives -= 3

            else:
                return "NO"

    return "YES"


def main():
    first_line = input()
    first_line = first_line.split()

    n = int(first_line[0])

    l = input().split()
    for i in range(len(l)):
        l[i] = int(l[i])

    print(possible_change(l))


main()
