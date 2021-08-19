def how_many(rows, cols):
    n = 0
    for i in range(len(rows)):
        if 'S' not in rows[i]:
            for j in range(len(cols)):
                rows[i][j] = 'E'
                cols[j][i] = 'E'
                n += 1
    for j in range(len(cols)):
        if 'S' not in cols[j]:
            n += cols[j].count('.')
    return n


def main():
    first_line = input()
    first_line = first_line.split()
    r = int(first_line[0])
    c = int(first_line[1])
    rows = []
    for i in range(r):
        line = input()
        rows += [list(line)]
    coloumns = [[rows[i][j] for i in range(r)] for j in range(c)]
    print(how_many(rows, coloumns))


main()
