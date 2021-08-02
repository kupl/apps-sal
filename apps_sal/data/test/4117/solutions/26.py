n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(n):
    for j in range(i):
        for k in range(j):
            if a[i] < a[k] + a[j] and a[i] != a[j] and a[j] != a[k]:
                ans += 1

print(ans)
