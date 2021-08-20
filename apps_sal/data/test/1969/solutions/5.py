def mi():
    return list(map(int, input().split()))


'\n5\n.....\n.XXX.\n.XXX.\n.XXX.\n.....\n'
n = int(input())
a = [0] * n
for i in range(n):
    a[i] = list(input())
cnt = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if a[i][j] == 'X' and a[i - 1][j - 1] == 'X' and (a[i + 1][j - 1] == 'X') and (a[i - 1][j + 1] == 'X') and (a[i + 1][j + 1] == 'X'):
            cnt += 1
print(cnt)
