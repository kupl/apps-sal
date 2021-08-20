def number_of_ones_if_flipped(l, from_index, to_index):
    counter = 0
    for i in range(len(l)):
        if not (from_index <= i and i <= to_index):
            if l[i] == 1:
                counter += 1
        elif l[i] == 0:
            counter += 1
    return counter


def all_possible_flips(l):
    maximum = -1 * float('inf')
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            if number_of_ones_if_flipped(l, i, j) > maximum:
                maximum = number_of_ones_if_flipped(l, i, j)
    return maximum


def main():
    first_line = input()
    first_line = first_line.split()
    n = int(first_line[0])
    l = input()
    l = l.split()
    for i in range(len(l)):
        l[i] = int(l[i])
    print(all_possible_flips(l))


main()
