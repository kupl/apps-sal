def R():
    return list(map(int, input().split()))


n = int(input())
f = list(R())
d = {}
for i in range(n):
    d[i + 1] = f[i]


def solve(d, n):
    for i in range(n):
        b = d[i + 1]
        c = d[b]
        a = d[c]
        if i + 1 == a:
            return 'YES'
    return 'NO'


print(solve(d, n))
