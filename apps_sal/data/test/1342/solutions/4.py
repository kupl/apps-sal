def judge(lists, x):
    ans = 0
    for i in lists:
        t = i // x
        d = i % x
        if d == 0:
            ans += t
        elif t + d >= x - 1:
            ans += t + 1
        else:
            return -1

    return ans


while True:
    try:
        n = input()
        balls = list(map(int, input().split()))
        minn = min(balls)
        for i in range(1, minn + 1):
            if judge(balls, minn // i + 1) >= 0:
                ans = judge(balls, minn // i + 1)
                break
            elif judge(balls, minn // i) >= 0:
                ans = judge(balls, minn // i)
                break

        print(ans)
    except EOFError:
        break
