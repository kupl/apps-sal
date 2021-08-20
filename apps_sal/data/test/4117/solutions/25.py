n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
ans = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            if a[i] + a[j] > a[k] and a[i] != a[j] and (a[j] != a[k]):
                ans += 1
print(ans)
