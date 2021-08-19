def calc(img):
    nr = len(img)
    nc = len(img[0])
    ret = 0
    for i in range(nr - 1):
        for j in range(nc - 1):
            tset = set()
            tset.add(img[i][j])
            tset.add(img[i][j + 1])
            tset.add(img[i + 1][j])
            tset.add(img[i + 1][j + 1])
            if 'f' in tset and 'a' in tset and ('c' in tset) and ('e' in tset):
                ret += 1
    return ret


def main():
    items = input().split()
    nr = int(items[0])
    nc = int(items[1])
    img = []
    for _ in range(nr):
        img.append(input())
    print(calc(img))


def __starting_point():
    main()


__starting_point()
