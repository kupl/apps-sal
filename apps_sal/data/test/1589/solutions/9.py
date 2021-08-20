(n, m) = list(map(int, input().split()))
ans = 0
for i in range(n):
    ints = list(map(int, input().split()))
    for j in range(m):
        if any(ints[2 * j:2 * j + 2]):
            ans += 1
print(ans)
