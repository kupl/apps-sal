def check(n, m, a):
    for i in range(n // 2):
        for j in range(m):
            if a[i][j] != a[-i - 1][j]:
                return 0
    if n % 2:
        return 0
    return 1


def new(n, a):
    return a[:(n + 1) // 2]


n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
cnt = 0
while (not (n % 2)) and check(n, m, a):
    a = new(n, a)
    n //= 2
print(len(a))
