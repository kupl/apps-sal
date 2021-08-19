def eat_cake(cols, rows, string):
    """
    >>> eat_cake(4, 3, ['S...', '....', '..S.'])
    8
    """
    result = 0
    for i in range(0, rows):
        if 'S' not in string[i]:
            result += cols
            string[i] = string[i].replace('.', 'E')
    for i in range(0, cols):
        contains = False
        all_eaten = True
        already_eaten = 0
        for j in range(0, rows):
            if string[j][i] == 'S':
                contains = True
            if string[j][i] == '.':
                all_eaten = False
            if string[j][i] == 'E':
                already_eaten += 1
        if all_eaten == False and contains == False:
            result += rows - already_eaten
            for row in range(0, rows):
                string[row] = string[row][0:i] + 'E' + string[row][i + 1:]
    return result


def main():
    first_line = input()
    first_line = first_line.split()
    rows = int(first_line[0])
    coloumns = int(first_line[1])
    l = []
    for i in range(rows):
        line = input()
        l.append(line)
    print(eat_cake(coloumns, rows, l))


main()
