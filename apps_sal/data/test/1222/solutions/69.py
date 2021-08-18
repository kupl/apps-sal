from collections import deque


def __starting_point():

    k = int(input())

    d = deque()
    ans = 0
    for i in range(1, 10):
        d.append(i)
    if k <= 9:
        print(k)
        return

    cnt = 9
    while True:
        x = d.popleft()
        if x % 10 != 0:
            tmp = 10 * x + (x % 10) - 1
            d.append(tmp)
            cnt += 1
            if cnt >= k:
                ans = tmp
                break

        tmp = 10 * x + (x % 10)
        d.append(tmp)
        cnt += 1
        if cnt >= k:
            ans = tmp
            break

        if x % 10 != 9:
            tmp = 10 * x + (x % 10) + 1
            d.append(tmp)
            cnt += 1
            if cnt >= k:
                ans = tmp
                break
    print(ans)


__starting_point()
