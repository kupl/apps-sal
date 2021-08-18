n, m = list(map(int, input().split()))
a = [[int(i) for i in input().split()]for _ in range(n)]
ans = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if a[i][j] == 0:
            temp = min(a[i + 1][j], a[i][j + 1]) - 1
            if temp > max(a[i - 1][j], a[i][j - 1]):
                ans += temp
                a[i][j] = temp
            else:
                print(-1)
                return
        else:
            ans += a[i][j]
            if 0 < i < n - 1:
                if a[i - 1][j] < a[i][j] < a[i + 1][j]:
                    continue
                else:
                    print(-1)
                    return
            if 0 < j < m - 1:
                if a[i][j - 1] < a[i][j] < a[i][j + 1]:
                    continue
                else:
                    print(-1)
                    return
print(ans)
