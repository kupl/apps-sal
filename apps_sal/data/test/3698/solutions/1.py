
def count_oper(x):
    if x == 1:
        return(0)

    res = 0
    y = x
    while y > 0:
        if y % 2 == 1:
            res += 1
        y = y // 2

    return(count_oper(res) + 1)


def solve(s, k):

    a = []
    ones = []
    for i in range(len(s)):
        c = s[i]
        a.append(int(c == '1'))
        if c == '1':
            ones.append(i)

    nones = len(ones)
    n = len(a)

    if k == 0:
        print(1)
        return

    if k == 1 and n != 1:
        print(n - 1)
        return

    if n == 1:
        if k > 0:
            print(0)
        else:
            print(1)
        return

    c = []
    c.append([0] * (n + 1))
    for n1 in range(1, n + 1):
        tmp = [0] * (n + 1)
        for m in range(n1 + 1):
            if m == 0 or m == n1:
                tmp[m] = 1
            else:
                tmp[m] = (c[n1 - 1][m - 1] + c[n1 - 1][m]) % modulo
        c.append(tmp)

    ans = 0
    for m in range(1, n + 1):
        if count_oper(m) == k - 1:
            for j in range(min(nones, m)):
                ans += (c[n - ones[j] - 1][m - j]) % modulo
            if nones >= m:
                ans += 1

    print(ans % modulo)


s = input()
k = int(input())

modulo = 10**9 + 7

solve(s, k)
