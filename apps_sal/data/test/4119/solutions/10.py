n, m = list(map(int, input().split()))
dots = list(map(int, input().split()))

if n >= m:
    print((0))
else:
    dots.sort()
    if n == 1:
        print((dots[-1] - dots[0]))
    else:
        dot_diffs = [[i, (dots[i + 1] - dots[i])] for i in range(len(dots) - 1)]
        dot_diffs.sort(key=lambda x: -x[1])
        ans = 0
        for idx, i in enumerate(dot_diffs[0:(n - 1)]):
            if idx == 0:
                ans += dots[i[0]] - dots[0]
            else:
                ans += dots[i[0]] - dots[prev[0] + 1]
            prev = i
        ans += dots[-1] - dots[dot_diffs[0:(n - 1)][-1][0] + 1]
        print(ans)
