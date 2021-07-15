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
    # print(f)
    print(f - original)


def averageSleepTime():
    n, k = list(map(int, input().split()))
    sleep = list(map(int, input().split()))
    run = 0
    for i in range(k):
        run += sleep[i]
    runavg = [run]
    for i in range(k, n):
        run = run - sleep[i - k] + sleep[i]
        runavg.append(run)
    print('{:.10f}'.format(sum(runavg)/(n-k+1)))


averageSleepTime()

