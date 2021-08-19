def abc128_d():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0

    for a in range(max(1, k + 1)):  # 左から取る個数
        for b in range(max(1, k - a + 1)):  # 右から取る個数
            if a + b > n:
                break
            arr = []
            if a > 0:
                arr += v[:a]
            if b > 0 and a < n:
                arr += v[max(a, 0, n - b):]
            arr.sort()
            for j in range(max(1, a + b)):  # 戻す個数
                if a + b + j > k:
                    break
                score = sum(arr[j:])
                ans = max(ans, score)
                #print(a, b, j, score, arr)
    print(ans)


def __starting_point():
    abc128_d()


__starting_point()
