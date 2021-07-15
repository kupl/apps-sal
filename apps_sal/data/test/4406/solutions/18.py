def __starting_point():
    l = [int(i) for i in input().split(" ")]
    n = l[0]
    k = l[1]

    l = [int(i) for i in input().split(" ")]

    a = []

    for i in l:
        if i not in a:
            if len(a)>=k:
                a.pop()
            a.insert(0,i)

    print(len(a))

    for i in a:
        print(i, end=' ')





__starting_point()
