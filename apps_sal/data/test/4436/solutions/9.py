from functools import reduce


def factors(n):
    k = sorted(list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5 + 1)) if n % i == 0)))))
    return k[1:]


t = int(input())
for _ in range(0, t):
    n = int(input())
    f = factors(n)
    if len(f) < 3:
        print('NO')
    else:
        ans = 'NO'
        (a, b, c) = (-1, -1, -1)
        for i in range(0, len(f)):
            for j in range(i + 1, len(f)):
                temp = n // f[i]
                temp //= f[j]
                if temp in f and temp != f[i] and (temp != f[j]):
                    (a, b, c) = (f[i], f[j], temp)
                    ans = 'YES'
                    break
            if ans == 'YES':
                break
        if ans == 'YES':
            print(ans)
            print(a, b, c)
        else:
            print(ans)
