n = int(input())
for i in range(n):
    num = int(input())
    temp = 1
    res = 0
    temp1 = 1
    slog = 1
    slog_temp = 11
    while temp <= num:
        if temp < 10 ** temp1:
            temp += slog
            res += 1
        else:
            temp = slog_temp
            temp1 += 1
            slog = slog_temp
            slog_temp = slog_temp + 10 ** temp1
    print(res)
