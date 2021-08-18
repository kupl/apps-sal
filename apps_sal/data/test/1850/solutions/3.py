

def __starting_point():

    n, d = [int(x) for x in input().split()]
    d -= 1
    s = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]

    val = p[0] + s[d]

    ans = 1

    t = n - (n - d) - 1

    for i in range(n - d, len(p)):

        if p[i] + s[t] > val:
            ans += 1
        else:
            t -= 1

    print(ans)


__starting_point()
