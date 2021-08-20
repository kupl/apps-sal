(n, k) = map(int, input().split())
a = list(map(str, input().split()))
ans = 0
for i in range(len(a)):
    if a[i].count('4') + a[i].count('7') <= k:
        ans += 1
print(ans)
