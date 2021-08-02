def check(n, d, x, y):
    if (y >= -x + d) and (y <= 2 * n - d - x) and (y <= d + x) and (y >= x - d):
        return True
    return False


n, d = list(map(int, input().split()))
m = int(input())
ans = []
for i in range(m):
    x, y = list(map(int, input().split()))
    if check(n, d, x, y):
        ans.append('YES')
    else:
        ans.append('NO')
for i in range(m):
    print(ans[i])
