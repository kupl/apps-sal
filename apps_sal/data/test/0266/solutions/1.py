(m, s) = list(map(int, str.split(input())))
if s == 0 and m == 1:
    print(0, 0)
elif s == 0 or s > 9 * m:
    print(-1, -1)
else:
    num = [0] * (m - 1) + [1]
    for i in range(m):
        num[i] += min(9, s - sum(num))
    a = str.join('', list(map(str, num[::-1])))
    num = [0] * m
    for i in range(m):
        num[i] = min(9, s - sum(num))
    b = str.join('', list(map(str, num)))
    print(a, b)
