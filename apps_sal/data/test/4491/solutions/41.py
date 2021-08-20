n = int(input())
a = [[], []]
a[0] = list(map(int, input().split()))
a[1] = list(map(int, input().split()))
ans = 0
for i in range(n):
    (x, sum) = (0, 0)
    for j in range(n + 1):
        if i == j - 1:
            x = 1
        sum += a[x][j - x]
    ans = max(sum, ans)
print(ans)
