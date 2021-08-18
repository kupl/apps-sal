def isOK(index, key, in_ls):
    if key < in_ls[index]:
        return True
    else:
        return False


def bs(in_ls, key):
    ng = -1
    ok = len(in_ls)
    while 1 < abs(ok - ng):
        mid = (ng + ok) // 2
        if isOK(mid, key, in_ls):
            ok = mid
        else:
            ng = mid
    return ok


def main():
    n = int(input())
    a_list = list(map(int, input().split(" ")))
    b_list = list(map(int, input().split(" ")))
    c_list = list(map(int, input().split(" ")))

    a_sorted = list(sorted(a_list))
    b_sorted = list(sorted(b_list))
    c_sorted = list(sorted(c_list))

    bc_dict = {}
    score = 0
    score_list = [0 for i in range(n)]
    for i, b in enumerate(b_sorted[::-1]):
        ok = bs(c_sorted, b)
        score += n - ok
        score_list[n - i - 1] += score

    total = 0
    for a in a_sorted:
        ok = bs(b_sorted, a)
        if ok == n:
            continue
        total += score_list[ok]

    print(total)


def __starting_point():
    main()


__starting_point()
