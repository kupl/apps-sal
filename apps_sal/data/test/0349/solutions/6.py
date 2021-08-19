(n, m) = list(map(int, input().split()))
(a1, a2) = ([], [])
for i in range(n):
    a1.append(list(map(int, input().split())))
for i in range(n):
    a2.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        (a1[i][j], a2[i][j]) = (min(a1[i][j], a2[i][j]), max(a1[i][j], a2[i][j]))


def check(a):
    for i in range(n):
        for j in range(1, m):
            if a[i][j] <= a[i][j - 1]:
                return False
    for j in range(m):
        for i in range(1, n):
            if a[i][j] <= a[i - 1][j]:
                return False
    return True


ans = 'Possible' if check(a1) and check(a2) else 'Impossible'
print(ans)
