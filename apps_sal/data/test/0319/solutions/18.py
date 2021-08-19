def read():
    return list(map(int, input().split()))


(n, m) = read()
a = []
for i in range(n):
    a.append(input())
ans = [0] * n
for i in range(m):
    ind = -1
    for j in range(n):
        if a[j][i] == '1':
            if ind != -1:
                ind = -1
                break
            ind = j
    if ind != -1:
        ans[ind] = 1
if 0 in ans:
    print('YES')
else:
    print('NO')
