(n, m) = map(int, input().split())
a = []
b = []
ans = 0
for i in range(n):
    a.append(list(input()))
for i in range(m):
    b.append(list(input()))
for i in range(n - m + 1):
    for j in range(n - m + 1):
        cnt = 0
        for s in range(m):
            for t in range(m):
                if b[s][t] == a[s + i][t + j]:
                    cnt += 1
        if cnt == m * m:
            ans = 1
if ans == 0:
    print('No')
else:
    print('Yes')
