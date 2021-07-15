n, m = list(map(int, input().split()))

if m == 0:
    print(n - 1)
else:
    div1 = set()
    min_div1 = 100001
    div2 = set()
    max_div2 = -1

    ans = 1

    for i in range(m):
        a, b = list(map(int, input().split()))
        x, y = max(a, b), min(a, b)

        if ans:
            if x < max_div2 or y > min_div1:
                ans = 0

            if x in div2 or y in div1:
                ans = 0

            div1.add(x)
            if x < min_div1:
                min_div1 = x

            div2.add(y)
            if y > max_div2:
                max_div2 = y

    # print(max_div2)
    # print(min_div1)

    if ans:
        for i in range(1, n + 1):
            if i not in div1 and i not in div2:
                if i > max_div2 and i < min_div1:
                    ans += 1


    print(ans)

