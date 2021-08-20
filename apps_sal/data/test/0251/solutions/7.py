def main():
    (n, k) = [int(x) for x in input().split(' ')]
    h = list([int(x) for x in input().split(' ')])
    num = [0 for i in range(max(h) + 5)]
    for i in h:
        num[i] += 1
    ans = 0
    now = max(h)
    now_cost = 0
    now_tower = 0
    while now:
        if num[now] + now_cost <= k:
            pass
        else:
            ans += 1
            now_cost = 0
        if num[now] == n:
            break
        now_cost += num[now]
        now -= 1
        num[now] += num[now + 1]
    if now_cost != 0:
        ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
