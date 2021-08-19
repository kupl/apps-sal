(n, m) = map(int, input().split())
t = []
cnt = 0
for i in range(n):
    t.append(input())
for i in range(n - 1):
    for j in range(m - 1):
        s = ''
        s += t[i][j]
        s += t[i + 1][j]
        s += t[i][j + 1]
        s += t[i + 1][j + 1]
        s = ''.join(sorted(list(s)))
        if s == 'acef':
            cnt += 1
print(cnt)
