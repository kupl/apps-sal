def fact(a, b):
    ans = 0
    while a % b == 0:
        ans += 1
        a //= b
    return ans


def fact_remove(a, b):
    c = a * b
    while c % 2 == 0:
        c //= 2
    while c % 3 == 0:
        c //= 3
    return c


a1, b1 = list(map(int, input().split(' ')))
a2, b2 = list(map(int, input().split(' ')))

if fact_remove(a1, b1) != fact_remove(a2, b2):
    print(-1)
else:
    ans = [0, 0, 0, 0]
    c1 = a1 * b1
    c2 = a2 * b2
    k1 = fact(c1, 3)
    k2 = fact(c2, 3)

    if k1 > k2:
        ans[1] = k1 - k2
        c1 /= 3**ans[1]
        c1 *= 2**ans[1]
    elif k1 < k2:
        ans[3] = k2 - k1
        c2 /= 3**ans[3]
        c2 *= 2**ans[3]

    k1 = fact(c1, 2)
    k2 = fact(c2, 2)
    if k1 > k2:
        ans[0] = k1 - k2
        c1 /= 2**ans[0]
    elif k1 < k2:
        ans[2] = k2 - k1
        c2 /= 2**ans[2]
    if c1 != c2:
        print(-1)
    else:
        print(sum(ans))
        while a1 % 3 == 0 and ans[1] > 0:
            a1 //= 3
            a1 *= 2
            ans[1] -= 1
        while a1 % 2 == 0 and ans[0] > 0:
            a1 //= 2
            ans[0] -= 1
        while b1 % 3 == 0 and ans[1] > 0:
            b1 //= 3
            b1 *= 2
            ans[1] -= 1
        while b1 % 2 == 0 and ans[0] > 0:
            b1 //= 2
            ans[0] -= 1
        while a2 % 3 == 0 and ans[3] > 0:
            a2 //= 3
            a2 *= 2
            ans[3] -= 1
        while a2 % 2 == 0 and ans[2] > 0:
            a2 //= 2
            ans[2] -= 1
        while b2 % 3 == 0 and ans[3] > 0:
            b2 //= 3
            b2 *= 2
            ans[3] -= 1
        while b2 % 2 == 0 and ans[2] > 0:
            b2 //= 2
            ans[2] -= 1
        print(a1, b1)
        print(a2, b2)
