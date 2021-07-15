def assign(s, n, k, c):
    res = []
    i = 0
    while k > 0 and i < n:
        if s[i] == 'o':
            res.append(i)
            k -= 1
            i += c
        i += 1
    return res


n, k, c = list(map(int, input().split()))
s = input()
a = assign(s, n, k, c)
b = assign(s[::-1], n, k, c)[::-1]
c = [n-x-1 for x in b]

for x, y in zip(a, c):
    if x == y:
        print((x + 1))

