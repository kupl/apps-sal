def read():
    return map(int, input().split())


def prime(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return 0
        d += 1
    return 1


t = int(input())
res = ''
for i in range(t):
    (a, b) = read()
    res += 'YES\n' if a - b == 1 and prime(a + b) else 'NO\n'
print(res)
