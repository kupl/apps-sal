n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 'YES'
for i in range(n - 1):
    if a[i] == a[i + 1]:
        ans = 'NO'
print(ans)
