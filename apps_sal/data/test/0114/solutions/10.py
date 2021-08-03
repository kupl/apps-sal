''' بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ '''
# codeforces1207B_live
def gi(): return list(map(int, input().split()))


n, m = gi()
a = [gi() for _ in range(n)]
b = [[0] * m for _ in range(n)]
ans = []
for k in range(n - 1):
    for j in range(m - 1):
        if a[k][j] == a[k][j + 1] == a[k + 1][j] == a[k + 1][j + 1] == 1:
            b[k][j] = b[k][j + 1] = b[k + 1][j] = b[k + 1][j + 1] = 1
            ans.append((k + 1, j + 1))
for k in range(n):
    for j in range(m):
        if a[k][j] != b[k][j]:
            print(-1)
            return
print(len(ans))
for e in ans:
    print(*e)
