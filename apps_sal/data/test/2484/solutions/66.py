def XorSum2():
    n = int(input())
    a = list(map(int, input().split()))
    ans, tmp0, tmp1 = 0, 0, 0

    # 尺取法インデックス
    right = 0

    for left in range(n):
        while right < n and tmp0 ^ a[right] == tmp1 + a[right]:
            tmp0 ^= a[right]
            tmp1 += a[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
            tmp0, tmp1 = 0, 0
        else:
            tmp0 ^= a[left]
            tmp1 -= a[left]
    print(ans)


def __starting_point():
    XorSum2()


__starting_point()
