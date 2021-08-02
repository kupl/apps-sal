def r():
    return list(map(int, input().split()))


n, m, k = r()
a = (k + 2 * m - 1) // (2 * m)
k -= (a - 1) * 2 * m
b = (k + 1) // 2
c = 'R' if k % 2 == 0 else 'L'
print(a, b, c)
