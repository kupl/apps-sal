for _ in range(int(input())):
    k = int(input())
    a = tuple(map(int, input().split()))
    cnt = sum(a)
    weeks, k = divmod(k - 1, cnt)
    ans = 1 << 32
    for i in range(7):
        x = 0
        for j in range(7):
            x += a[(i + j) % 7]
            if x == k + 1:
                ans = min(ans, j + 1)
                break
    print(7 * weeks + ans)
