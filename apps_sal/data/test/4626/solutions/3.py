for _ in range(int(input())):
    l = sorted(list(map(int, input().split())))
    ans = 2 * (l[2] - l[0])
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                L = list(l)
                L[0] += i
                L[1] += j
                L[2] += k
                L.sort()
                ans = min(ans, 2 * (L[2] - L[0]))
    print(ans)
