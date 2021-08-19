(n, k) = list(map(int, input().split()))
a = input().split()
ans = 0
for i in range(n):
    if a[i].count('4') + a[i].count('7') <= k:
        ans += 1
print(ans)
