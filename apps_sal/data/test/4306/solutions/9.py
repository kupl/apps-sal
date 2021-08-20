(a, b, c, d) = list(map(int, input().split()))
ans = 0
for i in range(201):
    if a <= i < b and c <= i < d:
        ans += 1
print(ans)
