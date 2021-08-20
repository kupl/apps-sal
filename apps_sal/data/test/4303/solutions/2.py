def __starting_point():
    (n, k) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans = float('inf')
    for i in range(k + 1):
        if i + k > n:
            break
        left = A[i]
        right = A[i + k - 1]
        tmp2 = abs(left) + abs(right - left)
        tmp3 = abs(right) + abs(left - right)
        ans = min(ans, min(tmp2, tmp3))
    print(ans)


__starting_point()
