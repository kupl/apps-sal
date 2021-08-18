from sys import stdin, stdout
from collections import deque
mod = 998244353
for _ in range(int(input())):
    n, m = list(map(int, stdin.readline().split()))
    a = [[] for i in range(n + 1)]
    length = [0] * (n + 1)
    if m == 0:
        print(pow(3, n, mod))
    else:
        d = []
        ans1 = 0
        ans2 = 0
        ans3 = 0
        for __ in range(m):
            x, y = list(map(int, stdin.readline().split()))
            a[x].append(y)
            a[y].append(x)
        col = [0] * (n + 1)
        de = deque([])
        for j in range(1, n + 1):
            if len(a[j]) == 0:
                ans3 += 1
            elif col[j] == 0:
                col[j] = 1
                de.append(j)
            c = 1
            c1 = 1
            while len(de):
                p = de.popleft()
                for i in a[p]:
                    if col[i] == 0:
                        col[i] = -col[p]
                        de.append(i)
                        if col[i] == 1:
                            c1 += 1
                        c += 1
            d.append([c, c1])

        flag = 0
        for i in range(1, n + 1):
            if flag == 1:
                break
            for j in a[i]:
                if col[i] == col[j]:
                    flag = 1
                    break
        k = 1
        if flag == 1:
            stdout.write(str(0) + '\n')
        else:
            for i in d:
                if i[0] != 1:
                    k1 = pow(2, i[1], mod)
                    k1 += pow(2, i[0] - i[1], mod)
                    k *= k1
            k *= pow(3, ans3, mod)
            k %= mod
            stdout.write(str(k) + '\n')
