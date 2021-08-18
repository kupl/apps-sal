def to4(num):
    if num // 4 < 1:
        return str(num)
    else:
        return to4(num // 4) + str(num % 4)


def SyntheticKadomatsu():
    idata = list(map(int, input().split()))
    l = [int(input()) for _ in range(idata[0])]
    ans = float('inf')
    for i in range(4**idata[0]):
        bits = [0] * 4
        tmp = 0
        num = to4(i).zfill(idata[0])
        for j in range(idata[0]):
            v = int(num[-j - 1])
            if bits[v] != 0 and v != 3:
                tmp += 10
            bits[v] += l[j]
        if 0 in set(bits[:-1]):
            continue
        for j in range(3):
            tmp += abs(bits[j] - idata[j + 1])
        ans = min(ans, tmp)
    print(ans)


def __starting_point():
    SyntheticKadomatsu()


__starting_point()
