def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def sum_applepie(list1, l):
    r = [i+l-1 for i in list1]
    return sum(r)


def main():
    n, l = Input()
    applepie = sum_applepie(list(range(1, n+1)), l)
    list2 = []
    for i in range(1, n+1):
        temp = []
        for j in range(1, n+1):
            if i == j:continue
            temp.append(j)
        k = sum_applepie(temp, l)
        list2.append((abs(applepie - k), k))
    print(sorted(list2, key=lambda x:x[0])[0][1])


main()
