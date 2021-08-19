def XXOR():
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    num = len(str(bin(10 ** 12))) - 2
    ans = 0
    for i in range(num, -1, -1):
        count = 0
        for j in a:
            if j >> i & 1:
                count += 1
        c = 2 ** i
        if count < n - count and c <= k:
            ans += (n - count) * c
            k -= c
        else:
            ans += count * c
    print(ans)


def __starting_point():
    XXOR()


__starting_point()
