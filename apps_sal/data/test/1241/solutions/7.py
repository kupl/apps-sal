def read_ints():
    return [int(x) for x in input().split()]


def main():
    n, k = read_ints()
    a = read_ints()

    lo = 0
    hi = 0
    count = 0
    x = -1
    y = -1
    while hi < n:
        if count < k or a[hi] != 0:
            if a[hi] == 0:
                count += 1
            if hi - lo >= y - x:
                x = lo
                y = hi
            hi += 1
        else:
            if a[lo] == 0:
                count -= 1
            lo += 1

    if x != -1:
        print(y - x + 1)
        for i in range(x, y + 1):
            a[i] = 1
        print(" ".join(map(str, a)))
    else:
        print(0)
        print(" ".join(map(str, a)))

main()

