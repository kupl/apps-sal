for gfhua in range(int(input())):
    n, m, x, y = list(map(int, input().split()))
    if y > x * 2:
        y = x * 2
    ans = 0
    for i in range(n):
        s = input()
        l = 0
        for j in s:
            if j == ".":
                l += 1
            else:
                ans += l // 2 * y + l % 2 * x
                l = 0
        ans += l // 2 * y + l % 2 * x
    print(ans)
