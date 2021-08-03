
ar = [
    [3, 3, -1, 4, 4, -1, 3, 3],
    [3, 3, -1, 4, 4, -1, 3, 3],
    [2, 2, -1, 3, 3, -1, 2, 2],
    [2, 2, -1, 3, 3, -1, 2, 2],
    [1, 1, -1, 2, 2, -1, 1, 1],
    [1, 1, -1, 2, 2, -1, 1, 1],
]

std = []


def main():
    mx = -1
    mq = -1
    mi = -1
    for q in range(6):
        s = input()
        std.append(s)
        for i in range(8):
            if(s[i] == '.' and ar[q][i] > mx):
                mx = ar[q][i]
                mq = q
                mi = i
    for q in range(6):
        s = ""
        for i in range(8):
            if(q == mq and i == mi):
                s += "P"
            else:
                s += std[q][i]
        print(s)


main()
