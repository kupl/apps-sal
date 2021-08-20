n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] % 2 == 0:
        while a[i] % 2 == 0:
            a[i] //= 2
            ans += 1
print(ans)
