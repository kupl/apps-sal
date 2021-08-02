K = int(input())
ans = 0
for i in range(1, K + 1, 2):
    for j in range(2, K + 1, 2):
        ans += 1
print(ans)
