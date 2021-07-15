def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    reds = [[int(item) for item in input().split()] for _ in range(N)]
    blues = [[int(item) for item in input().split()] for _ in range(N)]

    reds = sorted(reds, key=lambda x:x[1], reverse=True)
    blues.sort()

    que = collections.deque(blues)
    cnt = 0

    while que:

        bx, by = que.popleft()

        for rx, ry in reds[:]:
            if rx <= bx and ry <= by:
                cnt += 1
                reds.remove([rx, ry])
                break
    print(cnt)


def __starting_point():
    resolve()



__starting_point()
