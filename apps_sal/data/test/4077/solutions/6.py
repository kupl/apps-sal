def grCount(m, n, a):
    s = [0] * (2 * n + 1)
    sx = n
    result = 0
    s[sx] = 1
    add = 0
    for i in range(n):
        if a[i] < m:
            sx -= 1
            add -= s[sx]
        else:
            add += s[sx]
            sx += 1
        result += add
        s[sx] += 1
    return result


(n, m) = map(int, input().split())
a = list(map(int, input().split()))
print(grCount(m, n, a) - grCount(m + 1, n, a))
