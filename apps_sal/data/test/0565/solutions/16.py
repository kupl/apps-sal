(a, b, c) = list(map(int, input().split()))
ans = 0
for i in range(a + 1):
    if b >= i + 1 and c >= i + 2:
        ans = i * 3 + 3
print(ans)
