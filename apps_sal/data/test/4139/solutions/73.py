n = int(input())


def Base_10_to_n(X, n):
    if (int(X / n)):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


if n < 357:
    print((0))
else:
    ans = 0
    for i in range(3, 10):
        for j in range(3**i):
            a = ''
            val = Base_10_to_n(j, 3).zfill(i)
            for k in val:
                if k == '1':
                    a += '3'
                elif k == '2':
                    a += '5'
                else:
                    a += '7'
            if len(set(a)) == 3 and n >= int(a):
                ans += 1
    print(ans)
