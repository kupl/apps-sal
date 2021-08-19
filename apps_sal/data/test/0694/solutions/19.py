def solve(num, a, b):
    rem_a = [None] * len(num)
    rem_b = [None] * len(num)
    sn = num
    num = [int(x) for x in num]
    rem_a[0] = num[0] % a
    rem_b[-1] = num[-1] % b
    q = 1
    for i in range(1, len(num)):
        rem_a[i] = (rem_a[i - 1] * 10 + num[i]) % a
        q = q * 10 % b
        rem_b[-i - 1] = (num[-i - 1] * q + rem_b[-i]) % b
    for i in range(len(num) - 1):
        if rem_a[i] == 0 and rem_b[i + 1] == 0 and (num[i + 1] != 0):
            return (True, sn[:i + 1], sn[i + 1:])
    return (False, 0, 0)


def __starting_point():
    num = input()
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    (res, q, w) = solve(num, a, b)
    if res:
        print('YES')
        print(q)
        print(w)
    else:
        print('NO')


__starting_point()
