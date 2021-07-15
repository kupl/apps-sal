def __starting_point():
    n, m = list(map(int, input().split()))
    ans = []
    if m <= 2 * n:
        print(' '.join(str(i) for i in range(1, m + 1)))
    else:
        for i in range(1, (m - 2 * n + 1) // 2 + 1):
            ans.append(2 * n + 2 * i - 1)
            ans.append(2 * i - 1)
            if 2 * n + 2 * i <= m:
                ans.append(2 * n + 2 * i)
            ans.append(2 * i)        
        for i in range((m - 2 * n + 1) // 2 + 1, n + 1):
            ans.append(2 * i - 1)
            ans.append(2 * i)
        print(' '.join(str(i) for i in ans))
    

__starting_point()
