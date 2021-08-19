from sys import stdin, stdout


def __starting_point():
    (n, k) = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    num = [[] for i in range(200005)]
    ans = 200000 * 100
    for x in a:
        cnt = 0
        while x > 0:
            num[x].append(cnt)
            x //= 2
            cnt += 1
        num[x].append(cnt)
    for i in range(200001):
        if len(num[i]) < k:
            continue
        num[i].sort()
        cnt = 0
        for j in range(k):
            cnt += num[i][j]
        ans = min(ans, cnt)
    stdout.write('%d\n' % ans)


__starting_point()
