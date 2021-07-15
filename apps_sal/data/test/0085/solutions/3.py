a = [[0] * 2] * 2
s = [[[0] * 2, [0] * 2], [[0] * 2, [0] * 2]]
for i in range(2):
    a[i] = list(map(int, input().split()))
for i in range(2):
    for prime in range(2, 4):
        for j in range(2):
            t = a[i][j]
            while t % prime == 0:
                t //= prime
                s[i][prime - 2][j] += 1

ans = 0

for i in range(2):
    for prime in range(1, 2):
        mi = min(s[0][prime][0] + s[0][prime][1], s[1][prime][0] + s[1][prime][1]);
        j = 0
        while s[i][prime][0] + s[i][prime][1] > mi :
            if s[i][prime][j] == 0:
                j += 1
            a[i][j] //= prime + 2
            a[i][j] *= 2
            s[i][0][j] += 1
            s[i][prime][j] -= 1
            ans += 1

for i in range(2):
    for prime in range(1):
        mi = min(s[0][prime][0] + s[0][prime][1], s[1][prime][0] + s[1][prime][1]);
        j = 0
        while s[i][prime][0] + s[i][prime][1] > mi :
            if s[i][prime][j] == 0:
                j += 1
            a[i][j] //= prime + 2
            s[i][prime][j] -= 1
            ans += 1


if a[0][0] * a[0][1] != a[1][0] * a[1][1] :
    print(-1)
else :
    print(ans)
    print(a[0][0], a[0][1])
    print(a[1][0], a[1][1])

