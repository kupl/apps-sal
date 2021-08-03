n = int(input())
a = list(map(int, input().split()))
k = 0
ans = 0
while k != n:
    if ans % 2 == 0:
        for i in range(n):
            if a[i] <= k:
                k += 1
                a[i] = 10000
    else:
        for i in range(n - 1, -1, -1):
            if a[i] <= k:
                k += 1
                a[i] = 10000
    ans += 1
print(ans - 1)
