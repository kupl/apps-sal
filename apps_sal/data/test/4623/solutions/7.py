t = int(input())
for _ in range(t):
    n = int(input())
    ws = sorted(map(int, input().split()))
    ans = 0
    for s in range(2, 101):
        count = 0
        l = 0
        r = n - 1
        while r > l:
            if ws[l] + ws[r] == s:
                l += 1
                r -= 1
                count += 1
            elif ws[l] + ws[r] < s:
                l += 1
            else:
                r -= 1
        ans = max(ans, count)
    print(ans)
