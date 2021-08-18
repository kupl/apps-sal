

def __starting_point():
    n = int(input())
    orders = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        orders.append((b, a))

    sorders = sorted(orders)
    cnt = 0
    now = 1
    for i in range(0, len(sorders)):
        if sorders[i][1] > now or i == 0:
            cnt += 1
            now = sorders[i][0]
    print(cnt)


__starting_point()
