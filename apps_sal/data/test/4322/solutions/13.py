def create(s, e, cnt):
    arr = []
    for i in range(s, e + 1):
        arr.extend([i for _ in range(cnt[i] - 1)])
    arr.extend(list(range(e, s - 1, -1)))
    return arr


n = int(input())
a = list(map(int, input().split()))


def solve(a):
    cnt = [0] * 200001
    for x in a:
        cnt[x] += 1

    block = []
    max_ = 0
    i = 0
    s, e = None, None

    while i < len(cnt):
        if cnt[i] > 1:
            s = i
            while i + 1 < len(cnt) and cnt[i + 1] > 1:
                i += 1

            e = i
            if s >= 1 and cnt[s - 1] > 0:
                s -= 1
            if e + 1 < len(cnt) and cnt[e + 1] > 0:
                e += 1

            block.append([s, e])
            i = e + 1
        else:
            i += 1

    pos = -1
    for i, [s, e] in enumerate(block):
        sum_ = 0
        for j in range(s, e + 1):
            sum_ += cnt[j]

        if max_ < sum_:
            max_ = sum_
            pos = i

    if max_ >= 2:
        arr = create(block[pos][0], block[pos][1], cnt)
        return len(arr), ' '.join([str(x) for x in arr])
    else:
        for i in range(1, 200000):
            if cnt[i] == 1 and cnt[i + 1] == 1:
                return 2, str(i) + ' ' + str(i + 1)
        return 1, str(a[0])


length, arr = solve(a)

print(length)
print(arr)
