def read_int():
    return int(input())


def read_ints():
    return list(map(int, input().split(' ')))


d = [i % 10 for i in range(20)]


def one(n):
    digits = ['9' for i in range(n // 9)]
    if n % 9 != 0:
        digits.append(str(n % 9))
    digits.reverse()
    return ''.join(digits)


def two(n):
    if n % 2 == 1:
        if n <= 17:
            return n // 2
        return one((n - 17) // 2) + "8"
    else:
        if n < 10:
            return -1
        if n < 28:
            return (n - 9) // 2 * 10 + 9
        return one((n - 28) // 2) + "89"


def three(n):
    if n % 3 != 0:
        return - 1
    if n <= 24:
        return n // 3 - 1
    return one((n - 24) // 3) + "7"


def more(n, k):
    ans = int(1e50)
    for i in range(10):
        last = 0
        for j in range(i, i + k + 1):
            last += d[j]
        if last > n:
            continue
        if i + k < 10:
            if last == n:
                return i
            else:
                rem = n - last
                if rem % (k + 1) == 0:
                    up = int(one(rem // (k + 1))) * 10 + d[i]
                    ans = min(ans, up)
        else:
            right = i + k - 9
            left = k + 1 - right
            rem = n - last + left
            if rem % (k + 1) == 0:
                up = (int(one(rem // (k + 1))) - 1) * 10 + d[i]
                ans = min(ans, up)
    return -1 if ans == int(1e50) else ans


t = read_int()
for case_num in range(t):
    n, k = read_ints()
    print(more(n, k))
