def get_index(el, lst):
    for idx, element in enumerate(lst):
        if element == el:
            return idx

    return -1


def __starting_point():
    n, m, k = (int(cur_num) for cur_num in input().split())

    things = [int(cur_num) for cur_num in input().split()]

    ans = 0

    for _ in range(n):

        bought = [int(cur_num) for cur_num in input().split()]

        for purchase in bought:

            idx = get_index(purchase, things)

            ans += idx + 1

            del things[idx]

            things = [purchase] + things

    print(ans)


__starting_point()
