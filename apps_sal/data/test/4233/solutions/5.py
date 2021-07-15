n, m = list(map(int, input().split()))
arr = [input() for i in range(n)]
s1 = set()
s2 = set()
res = list()
for i in range(n):
    for j in range(m):
        if arr[i][j] == '*':
            s1.add((i, j))
            l = 1
            while True:
                if i - l >= 0 and i + l < n and j - l >= 0 and j + l < m:
                    if arr[i - l][j] == arr[i + l][j] == arr[i][j - l] == arr[i][j + l] == '*':
                        s2 |= {(i - l, j), (i + l, j), (i, j - l), (i, j + l)}
                        l += 1
                    else:
                        break
                else:
                    break
            l -= 1
            if l > 0:
                s2.add((i, j))
                res.append([i + 1, j + 1, l])
if len(s1 - s2) > 0:
    print(-1)
else:
    print(len(res))
    for x in res:
        print(*x)

