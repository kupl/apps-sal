N = int(input())
ans = 0
a = list(map(int, input().split()))
for i in range(N):
    while a[i] % 2 == 0:
        ans += 1
        a[i] = a[i] // 2
print(ans)
