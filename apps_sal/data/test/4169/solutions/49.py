n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(n)]

ab_sorted = sorted(ab, key=lambda x: (x[0], -x[1]))

num = 0
amount_of_money = 0
for i in range(n):
    buy = min(ab_sorted[i][1], m - num)
    num += buy
    amount_of_money += ab_sorted[i][0] * buy

    if num >= m:
        print(amount_of_money)
        return
