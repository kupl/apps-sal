for _ in range(int(input())):
    (n, k) = map(int, input().split())
    low = 1
    high = n - 1
    ans = n
    while low <= high:
        mid = (high + low) // 2
        temp = mid * (mid + 1) // 2
        if temp >= k:
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1
    temp = ans * (ans + 1) // 2 - k
    result = ['a'] * n
    result[n - ans - 1] = 'b'
    result[n - ans + temp] = 'b'
    print(''.join(result))
