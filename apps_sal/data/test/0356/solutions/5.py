def __starting_point():
    n1 = int(input().strip())
    a1 = [int(__) for __ in input().strip().split()]
    n2 = int(input().strip())
    a2 = [int(__) for __ in input().strip().split()]
    s1, s2 = sum(a1), sum(a2)
    if a1 == a2:
        print(n1)
    elif sum(a1) != sum(a2):
        print(-1)
    else:
        s1, s2 = 0, 0
        e1, e2 = n1 - 1, n2 - 1
        ans = 0
        while a1[s1] == a2[s2]:
            s1 += 1
            s2 += 1
            ans += 1
        while a1[e1] == a2[e2]:
            e1 -= 1
            e2 -= 1
            ans += 1
        p1 = [a1[s1]]
        p2 = [a2[s2]]
        for i in range(s1 + 1, e1 + 1):
            p1.append(p1[-1] + a1[i])
        for i in range(s2 + 1, e2 + 1):
            p2.append(p2[-1] + a2[i])
        d = {}
        for x in p1:
            d[x] = 1
        for x in p2:
            if x in d:
                ans += 1
        print(ans)


__starting_point()
