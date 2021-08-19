(n, deaph) = map(int, input().split())
buy = [0] * (10 ** 5 + 1)
sell = [0] * (10 ** 5 + 1)
for i in range(n):
    s = input()
    t = s[0]
    (c, v) = map(int, s[2:].split())
    if t == 'B':
        buy[c] += v
    elif t == 'S':
        sell[c] += v
ans_sell = []
cnt = 0
i = 0
while cnt < deaph and i < len(sell):
    if sell[i] != 0:
        ans_sell.append((i, sell[i]))
        cnt += 1
    i += 1
for i in range(len(ans_sell) - 1, 0 - 1, -1):
    print('S', ans_sell[i][0], ans_sell[i][1])
cnt = 0
i = len(buy) - 1
while cnt < deaph and i >= 0:
    if buy[i] != 0:
        print('B', i, buy[i])
        cnt += 1
    i -= 1
