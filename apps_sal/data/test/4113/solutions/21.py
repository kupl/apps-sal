n = int(input())
ans = 0
for i in range(n // 4 + 1):
    for j in range(n // 7 + 1):
        if i * 4 + j * 7 == n:
            ans = 1
print("Yes" if ans == 1 else "No")
