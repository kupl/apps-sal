def main():
    import math
    n = int(input())
    a = sorted(list(map(int, input().split())))
    if n == 2:
        print((a[1]))
        return
    ans = 0
    g = math.gcd(a[0], a[1])
    ans_list = []
    for i in range(1, int(g**0.5) + 1):
        if g % i == 0:
            ans_list.append(i)
    ans_list.append(g)
    for an in ans_list:
        cnt = 0
        for i in range(n):
            if a[i] % an != 0:
                cnt += 1
        if cnt < 2:
            if an > ans:
                ans = an
    g = math.gcd(a[1], a[2])
    ans_list = []
    for i in range(1, int(g**0.5) + 1):
        if g % i == 0:
            ans_list.append(i)
    ans_list.append(g)
    for an in ans_list:
        cnt = 0
        for i in range(n):
            if a[i] % an != 0:
                cnt += 1
        if cnt < 2:
            if an > ans:
                ans = an
    g = math.gcd(a[0], a[2])
    ans_list = []
    for i in range(1, int(g**0.5) + 1):
        if g % i == 0:
            ans_list.append(i)
    ans_list.append(g)
    for an in ans_list:
        cnt = 0
        for i in range(n):
            if a[i] % an != 0:
                cnt += 1
        if cnt < 2:
            if an > ans:
                ans = an
    print(ans)


def __starting_point():
    main()


__starting_point()
