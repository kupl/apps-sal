def soinsubunkai(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


def main():
    N = int(input())
    soinsu = {}
    for i in range(2, N + 1):
        i_soinsu = soinsubunkai(i)
        for (p, idx) in i_soinsu:
            if p not in soinsu:
                soinsu[p] = idx
            else:
                soinsu[p] += idx
    (n_75, n_25, n_15, n_5, n_3) = (0, 0, 0, 0, 0)
    for v in list(soinsu.values()):
        if v >= 74:
            n_75 += 1
        if v >= 24:
            n_25 += 1
        if v >= 14:
            n_15 += 1
        if v >= 4:
            n_5 += 1
        if v >= 2:
            n_3 += 1
    n_3_5_5 = n_5 * (n_5 - 1) * (n_3 - 2) // 2
    n_5_15 = n_15 * (n_5 - 1)
    n_3_25 = n_25 * (n_3 - 1)
    return n_3_5_5 + n_5_15 + n_3_25 + n_75


print(main())
