n = input()
a = list(map(int, input().split()))


def solve(a):
    flags = [0] * len(a)
    rec_flags = [0] * len(a)

    max1 = 0
    max2 = 0
    id_max1 = -1

    for i in range(len(a)):
        if a[i] < max2:
            pass
        elif a[i] > max1:
            max2 = max1
            max1 = a[i]
            id_max1 = i
            rec_flags[id_max1] += 1

        elif a[i] < max1 and a[i] > max2:
            flags[id_max1] += 1
            max2 = a[i]

    tar = max(flags)

    ans = []
    ans_no_rec = []
    if tar == 1:
        ind = flags.index(1)
        return min(a[ind:])
    else:
        for i in range(len(flags)):
            if flags[i] == tar:
                if rec_flags[i] > 0:
                    ans.append(a[i])
                else:
                    ans_no_rec.append(a[i])

    if ans_no_rec:
        return min(ans_no_rec)
    return min(ans)


print(solve(a))
