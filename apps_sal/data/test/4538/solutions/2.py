(n, d) = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
ans = 0
for (i, j) in x:
    if i ** 2 + j ** 2 <= d ** 2:
        ans += 1
print(ans)
