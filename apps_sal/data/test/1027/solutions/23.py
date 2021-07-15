rock = list(map(int, input().split()))
ma = 0
for i in range(14):
    cur_ma = 0
    cur = rock.copy()
    b = cur[i]
    cur[i] = 0
    for j in range(i + 1, 14):
        if b > 0:
            b -= 1
            cur[j] += 1
    for j in range(14):
        cur[j] += b // 14
    for j in range(b % 14):
        cur[j] += 1
    for elem in cur:
        if elem % 2 == 0:
            cur_ma += elem
    ma = max(ma, cur_ma)
print(ma)
