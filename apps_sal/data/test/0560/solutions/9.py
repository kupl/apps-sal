import sys


def main():
    cake = []
    r, c = list(map(int, sys.stdin.readline().split()))
    for i in range(r):
        cake.append(sys.stdin.readline().strip())
    row_count = 0
    for i in range(r):
        found_strawberry = False
        for j in range(c):
            if cake[i][j] == 'S':
                found_strawberry = True
                break
        if found_strawberry is False:
            row_count += 1
    col_count = 0
    for j in range(c):
        found_strawberry = False
        for i in range(r):
            if cake[i][j] == 'S':
                found_strawberry = True
                break
        if found_strawberry is False:
            col_count += 1
    print(row_count * c + col_count * r - row_count * col_count)


def __starting_point():
    return(main())


__starting_point()
