from collections import deque


def __starting_point():

    k = int(input())

    # ルンルン数のリストを先に作る必要がある
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
        # print("x="+str(x))
        # -1を入れる
        if x % 10 != 0:
            tmp = 10 * x + (x % 10) - 1
            # print(tmp)
            d.append(tmp)
            cnt += 1
            if cnt >= k:
                ans = tmp
                break

        # 同じ数を入れる
        tmp = 10 * x + (x % 10)
        # print(tmp)
        d.append(tmp)
        cnt += 1
        if cnt >= k:
            ans = tmp
            break

        # +1を入れる
        if x % 10 != 9:
            tmp = 10 * x + (x % 10) + 1
            # print(tmp)
            d.append(tmp)
            cnt += 1
            if cnt >= k:
                ans = tmp
                break
    print(ans)


__starting_point()
