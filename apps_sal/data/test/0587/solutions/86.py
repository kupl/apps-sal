def main():
    n, k = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(n)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    t = [0] * (n + 1)
    tmp = 0
    cnt = 0
    for i in range(k):
        ans += sushi[i][1]
        if t[sushi[i][0]] == 0:
            cnt += 1
        tmp += sushi[i][1]
        t[sushi[i][0]] += 1
    ans = tmp + cnt * cnt
    p = k
    for i in range(k, n):
        f = False
        if t[sushi[i][0]] == 0:
            f = True
            for j in reversed(range(p)):
                if 1 < t[sushi[j][0]]:
                    t[sushi[j][0]] -= 1
                    t[sushi[i][0]] += 1
                    tmp -= sushi[j][1]
                    tmp += sushi[i][1]
                    p = j
                    cnt += 1
                    ans = max(ans, tmp + cnt * cnt)
                    f = False
                    break
        if f:
            break
    print(ans)


def __starting_point():
    main()


__starting_point()
