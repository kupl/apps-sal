def main():
    n = int(input())
    inlis = list(map(int, input().split()))
    total = 0
    mae = 0
    for i in range(n):
        total += abs(inlis[i] - mae)
        mae = inlis[i]
    total += abs(inlis[-1])
    inlis.append(0)
    if 0 <= inlis[0] and inlis[0] > inlis[1]:
        if inlis[1] > 0:
            print(total - 2 * abs(inlis[1] - inlis[0]))
        else:
            print(total - 2 * abs(inlis[0]))
    elif 0 >= inlis[0] and inlis[0] < inlis[1]:
        if inlis[1] < 0:
            print(total - 2 * abs(inlis[1] - inlis[0]))
        else:
            print(total - 2 * abs(inlis[0]))
    else:
        print(total)
    for j in range(1, n):
        if inlis[j - 1] <= inlis[j] <= inlis[j + 1] or inlis[j - 1] >= inlis[j] >= inlis[j + 1]:
            print(total)
        elif inlis[j - 1] <= inlis[j] and inlis[j] > inlis[j + 1]:
            if inlis[j - 1] >= inlis[j + 1]:
                print(total - 2 * abs(inlis[j - 1] - inlis[j]))
            else:
                print(total - 2 * abs(inlis[j + 1] - inlis[j]))
        elif inlis[j - 1] >= inlis[j] and inlis[j] < inlis[j + 1]:
            if inlis[j - 1] >= inlis[j + 1]:
                print(total - 2 * abs(inlis[j + 1] - inlis[j]))
            else:
                print(total - 2 * abs(inlis[j - 1] - inlis[j]))


def __starting_point():
    main()


__starting_point()
