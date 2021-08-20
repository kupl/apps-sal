def count(val1, val2):
    digit = 1
    while digit * val2 <= val1:
        digit *= val2
    res = 0
    while digit != 1:
        cnt = int(val1 // digit)
        val1 -= digit * cnt
        res += cnt
        digit /= val2
    return (res, val1)


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
    ans = min(ans, int(res))
print(ans)
