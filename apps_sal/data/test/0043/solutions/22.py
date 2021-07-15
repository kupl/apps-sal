# FSX sb


def work():
    def dot(x, y):
        return x[0]*y[0]+x[1]*y[1]
    n = int(input())
    p = []
    for i in range(n):
        x, y = list(map(int, input().split(' ')))
        k = (20000 if y > 0 else -20000) if x == 0 else y / x
        l2 = x * x + y * y
        p.append((x, y, i+1, x >= 0, k, l2))
    p.sort(key=lambda item: (item[3], item[4]))
    p.append(p[0])
    ans1 = p[0][2]
    ans2 = p[1][2]
    ans_up = dot(p[0], p[1])
    ans_down = p[0][5]*p[1][5]
    for i in range(1, n):
        now_up = dot(p[i], p[i+1])
        now_down = p[i][5]*p[i+1][5]
        if (now_up >= 0 and ans_up <= 0) or (now_up > 0 and ans_up > 0 and (now_up * now_up * ans_down > ans_up * ans_up * now_down)) or (now_up < 0 and ans_up < 0 and (now_up * now_up * ans_down < ans_up * ans_up * now_down)):
            ans_up = now_up
            ans_down = now_down
            ans1 = p[i][2]
            ans2 = p[i + 1][2]
    print(ans1, ans2)


def __starting_point():
    work()

__starting_point()
