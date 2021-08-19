def count(val1, val2):
    num = 1
    while True:
        if val1 < val2 ** num:
            break
        num += 1
    cnt = 0
    digit = num
    while True:
        if val1 >= val2 ** digit:
            val1 -= val2 ** digit
            cnt += 1
        else:
            digit -= 1
        if digit == 0:
            break
    return (cnt, val1)


N = int(input())
ans = N
for i in range(0, N + 1):
    n = i
    m = N - i
    res = 0
    (cnt, nn) = count(n, 9)
    n = nn
    res += cnt
    (cnt, mm) = count(m, 6)
    m = mm
    res += cnt
    res += n + m
    ans = min(ans, res)
print(ans)
