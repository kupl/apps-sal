
n, x = list(map(int, input().split()))

pb = [[0] * 2 for i in range(n + 1)]
pb[0][0] = 1
pb[0][1] = 1
for i in range(1, n + 1):
    pb[i][0] = 3 + pb[i - 1][0] * 2
    pb[i][1] = 1 + pb[i - 1][1] * 2


def pbx(xx, nn):
    if nn == 0:
        return 1
    if xx == 1:
        return 0
    elif xx <= 1 + pb[nn - 1][0]:
        return pbx(xx - 1, nn - 1)
    elif xx == 2 + pb[nn - 1][0]:
        return pb[nn - 1][1] + 1
    elif xx <= 2 + pb[nn - 1][0] * 2:
        xxx = pbx(xx - pb[nn - 1][0] - 2, nn - 1)
        xxx = pb[nn - 1][1] + 1 + xxx
        return xxx
    elif xx == 3 + pb[nn - 1][0] * 2:
        return pb[nn][1]
    else:
        print(("----------", xx, nn))
        return 0


print((pbx(x, n)))
