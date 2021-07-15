from sys import stdin


def cost_of(data, k):
    kl = []
    for index, item in enumerate(data):
        kl.append(item + (index + 1) * k)
    kl.sort()

    accu = 0
    for i in range(0, k):
        accu += kl[i]

    return accu


n, s = list(map(int, stdin.readline().rstrip().split()))
data = list(map(int, stdin.readline().rstrip().split()))
left, right = 0, n
cleft, cright = 0, cost_of(data, n)

if s >= cright:
    print("{0} {1}".format(n, cright))
    return

last_center = -1
center = -1
while left <= right:
    last_center = center
    center = (left + right) // 2
    ccenter = cost_of(data, center)

    if center == last_center:
        rs = right if s >= cright else left
        left = rs
        break
    if s < ccenter:
        right = center - 1
        cright = cost_of(data, right)
    else:
        left = center
        cleft = cost_of(data, left)

print(left, cost_of(data, left))

