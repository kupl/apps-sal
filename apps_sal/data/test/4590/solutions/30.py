def main():
    line1 = input()
    line2 = input()
    line3 = input()
    (n, m, k) = list(map(int, line1.split()))
    a = [0] + list(map(int, line2.split()))
    b = [0] + list(map(int, line3.split()))
    (mark1, mark2) = (0, 0)
    for i in range(1, len(a)):
        a[i] += a[i - 1]
        if a[i] > k:
            mark1 = i
            break
    for i in range(1, len(b)):
        b[i] += b[i - 1]
        if b[i] > k:
            mark2 = i
            break
    if mark1:
        a = a[:mark1]
    if mark2:
        b = b[:mark2]
    ans = 0
    for i in range(len(a)):
        target = k - a[i]
        tmp = 0
        (low, high) = (0, len(b))
        while low < high:
            mid = (low + high) // 2
            if b[mid] <= target:
                tmp = mid
                low = mid + 1
            else:
                high = mid - 1
        ans = max(ans, i + tmp)
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
