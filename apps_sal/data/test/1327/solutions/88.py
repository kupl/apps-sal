def main():
    (n, m) = list(map(int, input().split()))
    info = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1 << 3):
        now_ans = [0] * n
        for j in range(3):
            d = 1
            if i >> j & 1:
                d *= -1
            for k in range(n):
                now_ans[k] += d * info[k][j]
        now_ans.sort(reverse=True)
        ans = max(ans, sum(now_ans[:m]))
    print(ans)


def __starting_point():
    main()


__starting_point()
