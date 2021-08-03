n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    while True:
        if a[i] % 2 == 0:
            ans += 1
            a[i] //= 2
        else:
            break

print(ans)
