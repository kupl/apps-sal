import sys


def main():
    n = int(sys.stdin.readline())
    mat = [None for __ in range(n)]
    for indx in range(n):
        mat[indx] = list(map(int, sys.stdin.readline().split()))

    good = True
    for row in range(n):
        for col in range(n):
            if mat[row][col] == 1:
                continue
            else:
                good &= check_this_element(mat, row, col)
    if good:
        print("Yes")
    else:
        print("No")


def check_this_element(mat, row, col):
    n = len(mat)
    for _row in range(n):
        for _col in range(n):
            if mat[_row][col] + mat[row][_col] == mat[row][col]:
                return True
    return False


def __starting_point():
    main()


__starting_point()
