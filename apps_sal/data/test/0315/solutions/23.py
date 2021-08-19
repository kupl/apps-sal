def __starting_point():
    #n = 4
    #k = 6
    #a = [2, 4, 3, 5]
    inp = input().split(' ')
    n = int(inp[0])
    k = int(inp[1])

    a = [int(ch) for ch in input().split(' ')]

    addition = 0
    for i in range(1, len(a)):
        sum = a[i - 1] + a[i]
        new_sum = k - sum
        if new_sum < 0:
            new_sum = 0
        addition += new_sum
        a[i] = a[i] + new_sum

    print(addition)

    res = ''
    for c in a:
        res = res + str(c) + ' '
    print(res)


__starting_point()
