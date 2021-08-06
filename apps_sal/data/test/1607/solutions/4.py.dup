n, k = list(map(int, input().split()))
limit = 998244353


if k > 2 * n:
    print(0)
elif k == 1 or k == 2 * n:
    print(2)
else:
    same = [0] * (k + 1)
    same[1] = 2

    diff = [0] * (k + 1)
    diff[2] = 2

    for i in range(2, n + 1):
        for j in range(min(k, 2 * i), 1, -1):

            same[j] = same[j] + 2 * diff[j] + same[j - 1]
            same[j] %= limit

            diff[j] = diff[j] + 2 * same[j - 1] + diff[j - 2]
            diff[j] %= limit

    print((same[k] + diff[k]) % limit)
