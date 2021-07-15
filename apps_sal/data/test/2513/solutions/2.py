def check(before, center, after, saying):
    return ([center, saying] in [["S", "o"], ["W", "x"]] and before == after)\
           or ([center, saying] in [["S", "x"], ["W", "o"]] and before != after)


def main():
    n = int(input())
    s = list(input())
    ans = "-1"
    for init in ["S", "W"]:
        if ans != "-1":
            break
        for next in ["S", "W"]:
            now_ans = ["" for _ in range(n)]
            now_ans[0] = init
            now_ans[1] = next
            for i in range(1, n - 1):
                if [now_ans[i], s[i]] in [["S", "o"], ["W", "x"]]:
                    now_ans[i + 1] = now_ans[i - 1]
                else:
                    now_ans[i + 1] = "W" if now_ans[i - 1] == "S" else "S"
            if check(now_ans[-2], now_ans[-1], now_ans[0], s[-1]) and check(now_ans[-1], now_ans[0], now_ans[1], s[0]):
                ans = "".join(now_ans)
                break
    print(ans)


def __starting_point():
    main()

__starting_point()
