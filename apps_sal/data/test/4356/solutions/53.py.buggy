n, m = map(int, input().split())
a = [input() for i in range(n)]
b = [input() for j in range(m)]
for i in range(n):
    for j in range(n - m + 1):
        tf = 0
        if a[i][j:j + m] == b[0] and i + m <= n:
            tf = 1
            for k in range(i + 1, i + m):
                if a[k][j:j + m] != b[k - i]:
                    tf = 0
        if tf:
            print('Yes')
            return
else:
    print('No')
