def main():
    n = int(input())
    digits = list(map(int, input()))
    enum = [digits]
    for a in range(1, 10):
        enum.append([(a + b) % 10 for b in digits])
    comp = []
    for i in range(10):
        if enum[i][0] == 0:
            comp.append(enum[i])
        for j in range(1, n):
            if enum[i][j] == 0 and enum[i][j - 1] != 0:
                comp.append(enum[i][j:] + enum[i][:j])
    print(''.join(map(str, min(comp))))


def __starting_point():
    main()


__starting_point()
