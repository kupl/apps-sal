a = list(map(int, input().split()))
p = sum(a)
ans = "NO"
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            if a[i] + a[j] + a[k] == p - (a[i] + a[j] + a[k]):
                ans = "YES"
                break
print(ans)

