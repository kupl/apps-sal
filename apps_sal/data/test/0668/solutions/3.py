n = int(input())
arr = [[i, int(c)] for (i, c) in enumerate(input().strip().split(' '))]
p = arr[0]
arr = arr[1:]
arr.sort(key=lambda i: i[1], reverse=True)
count = p[1]
i = 0
check = True
while i < len(arr):
    if count == 0:
        print(-1)
        check = False
        break
    count += arr[i][1]
    count -= 1
    i += 1
if check:
    ar = []
    count = 0
    cur = p
    (stock, stock_n) = ([], 0)
    i = 0
    while i < len(arr):
        ar.append([cur[0] + 1, arr[i][0] + 1])
        count += 1
        stock.append(arr[i])
        cur[1] -= 1
        if cur[1] == 0:
            cur = stock[stock_n]
            stock_n += 1
        i += 1
    print(count)
    for i in ar:
        print(i[0], i[1])
