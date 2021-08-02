from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 8:
        print(3)
        print(1, 0, 1)
    elif n == 4:
        print(2)
        print(0, 1)
    else:
        b = n.bit_length()
        ans = [1 << i for i in range(b)]
        t = 0
        c = 0
        n = 2 ** b - 1 - n
        for i in range(1, b):
            if (n >> (b - i)) & 1:
                t += 1
                c += 1
            ans[i] -= t
            t *= 2
        ans[-1] -= (c + (n & 1))
        res = [0] * (b - 1)
        for i in range(b - 1):
            res[i] = ans[i + 1] - ans[i]
        print(b - 1)
        print(' '.join(map(str, res)))
