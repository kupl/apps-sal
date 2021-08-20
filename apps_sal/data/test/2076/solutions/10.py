t = int(input())
for _ in range(t):
    (a, b, c) = map(int, input().split())
    ans = 0
    cnt_2 = min(c // 2, b)
    ans += cnt_2 * 3
    b -= cnt_2
    c -= cnt_2 * 2
    cnt_1 = min(a, b // 2)
    ans += cnt_1 * 3
    print(ans)
