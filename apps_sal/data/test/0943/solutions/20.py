def __starting_point():

    n = int(input())
    a = [int(x) for x in input().split()]

    the_sum = sum(a)

    if the_sum % 2 == 0:
        print(the_sum)
    else:
        max_num = max(a)
        min_odd = max_num + 1
        for aa in a:
            if aa%2 == 1 and aa < min_odd:
                min_odd = aa

        if min_odd == max_num + 1:
            print(0)
        else:
            print( the_sum -  min_odd )

__starting_point()
