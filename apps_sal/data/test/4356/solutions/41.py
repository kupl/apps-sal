(n, m) = map(int, input().split())
a = [list(input()) for i in range(n)]
b = [list(input()) for i in range(m)]
exist = False
for i in range(n - m + 1):
    for j in range(n - m + 1):
        match = True
        for k in range(m):
            for l in range(m):
                if a[i + k][j + l] != b[k][l]:
                    match = False
        if match:
            exist = True
print('Yes' if exist else 'No')
