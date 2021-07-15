T = int(input())
for _ in range(T):
    n, x, y = list(map(int, input().split()))

    if x > y:
        x, y = y, x

    ans1 = 1 if x + y <= n else x + y - n + 1

    if ans1 > n:
        ans1 -= 1

    ans2 = n if x + y > n else x + y - 1

    print(ans1, ans2)

