def main():
    c = [list(map(int, input().split())) for _ in [0, 0, 0]]
    for j in [2, 1, 0]:
        if c[j][0] - c[j - 1][0] == c[j][1] - c[j - 1][1] == c[j][2] - c[j - 1][2]:
            continue
        if c[0][j] - c[0][j - 1] == c[1][j] - c[1][j - 1] == c[2][j] - c[2][j - 1]:
            continue
        print("No")
        return
    print("Yes")
    return


main()
