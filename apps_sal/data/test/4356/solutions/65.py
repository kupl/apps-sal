(n, m) = map(int, input().split())
a = [input() for i in range(n)]
b = [input() for i in range(m)]
ans = False
for i in range(n - m + 1):
    for j in range(n - m + 1):
        part_a = [a[y][j:j + m] for y in range(i, i + m)]
        cnt = 0
        for k in range(m):
            for l in range(n - m + 1):
                if part_a[k][l:m + l] == b[k]:
                    cnt += 1
        if cnt == m:
            ans = True
if ans:
    print('Yes')
else:
    print('No')
