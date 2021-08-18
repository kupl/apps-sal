K = int(input())


def ns(n):
    ret, tmp = 0, n

    while tmp > 0:
        r = tmp % 10
        tmp //= 10
        ret += r

    return ret


ans, base = 0, 1
for _ in range(K):
    ans += base
    print(ans)

    if (ans + base) / ns(ans + base) > (ans + 10 * base) / ns(ans + 10 * base):
        base *= 10
