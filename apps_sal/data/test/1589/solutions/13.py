def read():
    return list(map(int, input().split()))


(n, m) = read()
a = [list(read()) for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][2 * j + 1] == 1 or a[i][2 * j] == 1:
            cnt += 1
print(cnt)
