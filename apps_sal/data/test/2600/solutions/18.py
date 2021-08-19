for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    arr = [[0] * m for i in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    ans = 0
    brr = []
    for s in range(n + m - 1):
        kek = [0, 0]
        for i in range(n):
            j = s - i
            if not 0 <= j < m:
                continue
            kek[arr[i][j]] += 1
        brr.append(kek)
    for i in range(len(brr) // 2):
        ans += min(brr[i][0] + brr[-i - 1][0], brr[i][1] + brr[-i - 1][1])
    print(ans)
