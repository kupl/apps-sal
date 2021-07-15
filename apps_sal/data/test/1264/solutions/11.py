n = int(input())
bs = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i, n):
        ans = max(ans, sum(bs) + j - i + 1 - 2 * sum(bs[i: j + 1]))
print(ans)

