n, m, k = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
ans = 0
for i in range(n):
    st = 0
    for j in range(m):
        if a[i][j] == '.':
            st += 1
            if st >= k:
                ans += 1
        else:
            st = 0
for i in range(m):
    st = 0
    for j in range(n):
        if a[j][i] == '.':
            st += 1
            if st >= k:
                ans += 1
        else:
            st = 0
if k == 1:
    print(int(ans / 2))
else:
    print(ans)
