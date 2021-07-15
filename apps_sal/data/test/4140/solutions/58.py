def resolve():
    '''
    code here
    '''
    S = input()

    ans1 = 0
    res1 = 0
    ans2 = 1
    res2 = 0
    for item in S:
        item = int(item)
        if ans1%2 != item:
            res1 += 1
        if ans2%2 != item:
            res2 += 1

        ans1 += 1
        ans2 += 1

    print((min(res2, res1))) 


def __starting_point():
    resolve()

__starting_point()
