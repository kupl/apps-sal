(a, b) = map(int, input().split())
ans = 0
for i in range(1, a):
    for j in range(1, 13):
        if i == j:
            ans += 1
for i in range(a, a + 1):
    for j in range(1, b + 1):
        if i == j:
            ans += 1
print(ans)
