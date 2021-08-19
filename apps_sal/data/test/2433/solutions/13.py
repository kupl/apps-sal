for _ in range(int(input())):
    (b, p, f) = list(map(int, input().split()))
    (h, c) = list(map(int, input().split()))
    ans = 0
    for beef in range(p + 1):
        buns = b - 2 * beef
        chick = min(buns // 2, f)
        if buns < 0:
            continue
        ans = max(ans, beef * h + c * chick)
    print(ans)
