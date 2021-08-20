x = int(input())
ans = 0
for i in range(2, 11):
    for j in range(1, x + 1):
        if x >= j ** i:
            ans = max(ans, j ** i)
print(ans)
