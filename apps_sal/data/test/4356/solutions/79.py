(n, m) = list(map(int, input().split()))
a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(m)]
r = n - m + 1
for x in range(r ** 2):
    for y in range(m ** 2):
        if a[x // r + y // m][x % r + y % m] != b[y // m][y % m]:
            break
    else:
        print('Yes')
        break
else:
    print('No')
