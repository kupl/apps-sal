def max(a, b):
    if a > b:
        return a
    else:
        return b


def min(a, b):
    if a < b:
        return a
    else:
        return b


def __starting_point():
    n = int(input())
    A = input().split(' ')
    (ans, count, Min, Max) = (0, 0, 1000000000, -100000000000)
    for i in range(n):
        now = int(A[i])
        if now % 2 == 0:
            ans += max(now, 0)
        elif now < 0:
            Max = max(Max, now)
        else:
            Min = min(Min, now)
            ans += now
    if ans % 2 == 0:
        ans = max(ans - Min, ans + Max)
    print(ans)


__starting_point()
