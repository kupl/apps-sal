def main():
    strnum = input()
    odd = int(strnum[-1])
    maxpos = -1
    minpos = -1
    l = len(strnum)
    for i in range(l):
        d = int(strnum[i])
        if d % 2 == 0:
            if d < odd:
                maxpos = i
                break
            else:
                minpos = i

    if maxpos > -1:
        for i in range(l):
            if i == maxpos:
                print(odd, end="")
            elif i == l-1:
                print(strnum[maxpos])
            else:
                print(strnum[i], end="")
    elif minpos > -1:
        for i in range(l):
            if i == minpos:
                print(odd, end="")
            elif i == l-1:
                print(strnum[minpos])
            else:
                print(strnum[i], end="")
    else:
        print(-1)


main()

