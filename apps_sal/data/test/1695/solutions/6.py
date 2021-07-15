n, m = map(int, input().split())
a = [list(input()) for i in range(n)]
count = [[0 for i in range(5)] for i in range(m)]
b = list(map(int, input().split()))
for i in range(n):
    for j in range(m):
        count[j][ord(a[i][j]) - ord("A")] += 1
ans = 0
for i in range(m):
    ans += max(count[i]) * b[i]
print(ans)
