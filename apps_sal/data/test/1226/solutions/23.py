n, a, b = list(map(int, input().split()))
M = 10**9 + 7


def combination(n, k):
    if k > n - k:
        k = n - k
    if k == 0:
        return 1
    if k == 1:
        return n
    p = [-1 for i in range(k + 1)]
    kp = {i: [] for i in range(n - k + 1, n + 1)}
    count = [0 for i in range(k + 1)]
    for i in range(2, k + 1):
        if p[i] == -1:
            for j in range(i, k + 1, i):
                if p[j] == -1:
                    p[j] = i
            for j in range(((n - k) // i + 1) * i, n + 1, i):
                kp[j].append(i)
    for i in range(2, k + 1):
        j = i
        while p[j] != -1:
            m = p[j]
            while j % m == 0:
                count[m] += 1
                j = j // m
    ans = 1
    for i in kp:
        bufi = i
        for j in kp[i]:
            while count[j] > 0 and bufi % j == 0:
                bufi = bufi // j
                count[j] -= 1
        ans *= bufi
        ans %= M

    return ans


print(((pow(2, n, M) - 1 - combination(n, a) - combination(n, b)) % M))
