3


def main():
    n, h = list(map(int, input().split()))
    leng = 0
    for ai in map(int, input().split()):
        if ai <= h:
            leng += 1
        else:
            leng += 2

    print(leng)


main()
