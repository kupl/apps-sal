def main():
    l = list(input().split())
    word = list(l[1])
    count = 0
    for i in range(int(l[0])):
        at_num = 0
        cg_num = 0
        for j in word[i:int(l[0])]:
            if j == 'A':
                at_num += 1
            elif j == 'T':
                at_num -= 1
            elif j == 'G':
                cg_num += 1
            elif j == 'C':
                cg_num -= 1
            if at_num == 0 and cg_num == 0:
                count += 1
    print(count)


def __starting_point():
    main()


__starting_point()
