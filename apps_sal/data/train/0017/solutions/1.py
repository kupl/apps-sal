
from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    l = [0] * (n + 1)
    ans = 0

    for j in range(n):
        r = [0] * (n + 1)
        for k in range(n - 1, j, -1):
            ans += l[a[k]] * r[a[j]]
            r[a[k]] += 1
        l[a[j]] += 1

    print(ans)
