def mi():
    return list(map(int, input().split()))


'''
3 3
1 1 1
1 1 1
0 1 1
'''
n, m = mi()
a = [0] * n
for i in range(n):
    a[i] = list(mi())
out = []
b = [[0] * m for i in range(n)]
for i in range(n - 1):
    for j in range(m - 1):
        if a[i][j] == 1 and a[i + 1][j] == 1 and a[i + 1][j + 1] == 1 and a[i][j + 1] == 1:
            out.append(str(i + 1) + ' ' + str(j + 1) + '\n')
            b[i][j] = b[i + 1][j] = b[i + 1][j + 1] = b[i][j + 1] = 1
        if a[i][j] != b[i][j]:
            print(-1)
            return
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            return
print(len(out))
print(''.join(out))
