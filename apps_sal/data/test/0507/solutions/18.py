def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans_list = [-3 for i in range(n)]

    mismatch_count = 0
    ans_set = set([])
    for i in range(0, n):
        if a[i] == b[i]:
            ans_list[i] = a[i]
            ans_set.add(a[i])
        else:
            mismatch_count += 1
            ans_list[i] += mismatch_count

    one_to_n_set = set([i for i in range(1, n + 1)])
    add_set = one_to_n_set.difference(ans_set)
    if mismatch_count == 1:
        ans_list[ans_list.index(-2)] = add_set.pop()
    else:
        tmp1 = ans_list.index(-2)
        tmp2 = ans_list.index(-1)
        ele1 = add_set.pop()
        ele2 = add_set.pop()
        if ele1 == a[tmp1] and ele2 == b[tmp2]:
            ans_list[tmp1] = ele1
            ans_list[tmp2] = ele2
        elif ele1 == a[tmp2] and ele2 == b[tmp1]:
            ans_list[tmp2] = ele1
            ans_list[tmp1] = ele2
        elif ele2 == a[tmp1] and ele1 == b[tmp2]:
            ans_list[tmp1] = ele2
            ans_list[tmp2] = ele1
        elif ele2 == a[tmp2] and ele1 == b[tmp1]:
            ans_list[tmp2] = ele2
            ans_list[tmp1] = ele1

    for i in range(0, n):
        print(ans_list[i], end=' ')


__starting_point()
