l = input().split(' ')
x = int(l[0])
k = int(l[1])

if x == 0:
    print('0')
else:
    mod = 1000000007

    def pow_mod(a, b):
        if b < 2:
            return int(a ** b) % mod
        elif b % 2 == 0:
            return int(pow_mod(a, b // 2) ** 2) % mod
        else:
            return pow_mod(a, b - 1) * a % mod

    twop = pow_mod(2, k)
    high = x * twop
    leafs = twop
    low = high - leafs + 1
    s = (high + 1) * high // 2 - (low - 1 + 1) * (low - 1) // 2
    answer = s * 2 // leafs
    answer %= mod

    print(answer)
