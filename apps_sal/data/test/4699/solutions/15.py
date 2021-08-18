N, K = map(int, input().split())
hate_num = list(map(int, input().split()))
i = N

while 1:
    ans = list({int(i) for i in list(str(i))})
    for j in ans:
        if j in hate_num:
            break
    else:
        print(i)
        break
    i += 1
