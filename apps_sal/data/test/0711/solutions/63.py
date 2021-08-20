def factorization(n):
    (primen, degree, primend) = ([], [], [])
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            primen.append(i)
            degree.append(cnt)
            primend.append([i, cnt])
    if temp != 1:
        primen.append(temp)
        degree.append(1)
        primend.append([temp, 1])
    if primen == []:
        primen.append(n)
        degree.append(1)
        primend.append([n, 1])
    return degree


def main():
    (N, M) = map(int, input().split())
    if M == 1:
        print(1)
    else:
        mod = 10 ** 9 + 7
        Mf = factorization(M)
        l = max(Mf)
        Comb = [1] * (l + 1)
        for i in range(1, l + 1):
            tmp = Comb[i - 1]
            tmp *= N - 1 + i
            tmp *= pow(i, mod - 2, mod)
            Comb[i] = tmp % mod
        ret = 1
        for i in Mf:
            ret *= Comb[i]
            ret %= mod
        print(ret)


def __starting_point():
    main()


__starting_point()
