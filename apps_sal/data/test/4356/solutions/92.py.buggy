n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in range(n - m + 1):
    for j in range(n - m + 1):
        tnp = 0
        for k in range(m):
            for l in range(m):
                if (a[i + k][j + l] != b[k][l]):
                    tnp += 1
        if (tnp == 0):
            print("Yes")
            return
print("No")
