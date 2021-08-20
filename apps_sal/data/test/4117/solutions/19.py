n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if l[i] == l[j]:
            continue
        for k in range(j + 1, n):
            if l[i] != l[k] != l[j] and max(l[i], l[j], l[k]) < l[i] + l[j] + l[k] - max(l[i], l[j], l[k]):
                ans += 1
print(ans)
