def count_lucky_numbers(l):
    counter = 0
    for i in range(len(l)):
        if l[i] == '4' or l[i] == '7':
            counter += 1
    return counter


def how_many_below(l, k):
    counter = 0
    for item in l:
        if count_lucky_numbers(item) <= k:
            counter += 1
    return counter


def main():
    first_line = input()
    first_line = first_line.split()

    n = int(first_line[0])
    k = int(first_line[1])

    l = input()
    l = l.split()

    print(how_many_below(l, k))


main()
