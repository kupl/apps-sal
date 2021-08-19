def GI():
    return int(input())


def GIS():
    return list(map(int, input().split()))


def LGIS():
    return list(GIS())


def main():
    for t in range(GI()):
        s = sorted(input())
        for i in range(len(s) - 1):
            if ord(s[i + 1]) - ord(s[i]) != 1:
                print('No')
                break
        else:
            print('Yes')


main()
