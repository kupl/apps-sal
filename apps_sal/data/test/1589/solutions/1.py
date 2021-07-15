n, m = list(map(int, input().split()))
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    for t in range(m):
        if a[t * 2] == 1 or a[t * 2 + 1] == 1:
            ans += 1
print(ans)

