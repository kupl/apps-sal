s = 'codeforces'
a = [1] * len(s)
ans, cp, n = 1, 0, len(s)
k = int(input())
while ans < k:
    ans = ans // a[cp]
    a[cp] += 1
    ans *= a[cp]
    cp = (cp + 1) % n
print(''.join([s[x] * y for x, y in enumerate(a)]))
