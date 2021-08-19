def luckyYear():
    n = int(input())
    original = n
    p = -1
    f = 0
    while n > 0:
        f = n % 10
        n //= 10
        p += 1
    f += 1
    f *= 10 ** p
    print(f - original)


def averageSleepTime():
    (n, k) = list(map(int, input().split()))
    sleep = list(map(int, input().split()))
    run = 0
    for i in range(k):
        run += sleep[i]
    runavg = [run]
    for i in range(k, n):
        run = run - sleep[i - k] + sleep[i]
        runavg.append(run)
    print('{:.10f}'.format(sum(runavg) / (n - k + 1)))


def teaParty():
    (n, w) = list(map(int, input().split()))
    tea = list(map(int, input().split()))
    fill = []
    [fill.append((t + 1) // 2) for t in tea]
    if sum(tea) < w or sum(fill) > w:
        print(-1)
        return
    w -= sum(fill)
    sortedPos = [i[0] for i in sorted(enumerate(tea), key=lambda x: x[1])]
    for i in sortedPos[::-1]:
        if w <= 0:
            break
        value = min(tea[i] - fill[i], w)
        fill[i] += value
        w -= value
    print(' '.join(map(str, fill)))


teaParty()
