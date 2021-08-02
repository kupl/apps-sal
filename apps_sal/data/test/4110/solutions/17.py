D, G = list(map(int, input().split()))
pc = [list(map(int, input().split())) for i in range(D)]

ans = float("inf")

for bit in range(1 << D):
    count = 0
    sum = 0
    rest = list(range(1, D + 1))

    for i in range(D):
        if bit & (1 << i):
            sum += (i + 1) * pc[i][0] * 100 + pc[i][1]
            count += pc[i][0]
            rest.remove(i + 1)

    if sum < G:
        max_num = max(rest)
        n = min(pc[max_num - 1][0], -(-(G - sum) // (max_num * 100)))
        count += n
        sum += n * max_num * 100

    if sum >= G:
        ans = min(ans, count)

print(ans)
