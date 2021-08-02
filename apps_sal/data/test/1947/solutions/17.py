def CuttingTime(hairline_len, l, time, p, d):
    n = len(list(hairline_len.keys()))
    if hairline_len[p] <= l:
        hairline_len[p] += d
        if p == 1:
            if n > 1:
                if hairline_len[p + 1] <= l and hairline_len[p] > l:
                    time += 1
            else:
                if hairline_len[p] - d <= l:
                    time += 1
        elif 1 < p < n:
            if hairline_len[p] > l:
                if hairline_len[p - 1] <= l and hairline_len[p + 1] <= l:
                    time += 1
                elif hairline_len[p - 1] > l and hairline_len[p + 1] > l and time > 1:
                    time -= 1
        else:
            if hairline_len[p - 1] <= l and hairline_len[p] > l:
                time += 1

    return time


def InitialTIme(hairline_len, l):
    time = 0
    count = 0

    for i in hairline_len:
        if hairline_len[i] > l:
            count += 1
        else:
            if count > 0:
                time += 1
            count = 0

    if count > 0:
        time += 1

    return time


def AliceHairDresser():
    inputs = list(map(int, input().split()))
    n = inputs[0]
    m = inputs[1]
    l = inputs[2]

    lengths = list(map(int, input().split()))
    hairline_len = {}

    for i in range(1, n + 1):
        hairline_len[i] = lengths[i - 1]

    time = InitialTIme(hairline_len, l)
    # print time

    for i in range(m):
        query = input()

        if len(query) == 1:
            print(time)
        else:
            inputs1 = list(map(int, query.split()))
            # print inputs1
            p = inputs1[1]
            d = inputs1[2]
            if hairline_len[p] <= l:
                time = CuttingTime(hairline_len, l, time, p, d)


AliceHairDresser()
