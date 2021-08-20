(n, k) = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort()


def slv():
    cnt = 0
    for i in range(n):
        cnt += ab[i][1]
        if cnt >= k:
            return print(ab[i][0])


slv()
