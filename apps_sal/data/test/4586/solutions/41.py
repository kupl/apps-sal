def iroha():
    num = list(input())
    count = 0
    head = num[0]

    for i, char in enumerate(num):
        if head == num[i]:
            count += 1
            if count >= 3:
                print('Yes')
                return
        else:
            count = 1
            head = num[i]

    print('No')


def __starting_point():
    iroha()


__starting_point()
