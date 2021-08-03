mem = [[-1 for j in range(201)] for i in range(1 << 10)]


def dp(i, j, n, m, a, b):
    if(j == n):
        return 0
    if(mem[i][j] != -1):
        return mem[i][j]
    ans = 1 << 10
    for k in range(m):
        ans = min(ans, (i | (a[j] & b[k])) | dp(i | (a[j] & b[k]), j + 1, n, m, a, b))
    mem[i][j] = ans
    return ans


n, m = map(int, input().split())
a = [*map(int, input().split())]
ans = 0
b = [*map(int, input().split())]
print(dp(0, 0, n, m, a, b))
