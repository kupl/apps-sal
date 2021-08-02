def main():
    n = int(input())
    ss = [i for i in input().split(' ')]

    nss = []
    for i in range(len(ss)):
        arr = []
        for c in ss[i]:
            if not c in arr:
                arr.append(c)
        arr.sort()
        ns = ''.join(arr)

        if not ns in nss:
            nss.append(ns)

    print(len(nss))


main()
