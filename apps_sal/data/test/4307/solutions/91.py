n = int(input())
ans = 0
for i in range(1, n + 1, 2):
    con = 0
    for j in range(1, i + 1):
        if i % j == 0:
            con += 1
        if con == 8:
            ans += 1
print(ans)
