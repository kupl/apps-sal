def pal(s):
    return s == s[::-1]


s, k = input(), int(input())
if len(s) % k != 0:
    print('NO')
else:
    n = len(s) // k
    print('YES' if all(pal(s[i * n:(i + 1) * n]) for i in range(k)) else 'NO')
