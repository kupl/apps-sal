n = int(input())
a = list(map(int, input().split()))
sv = 0
ans = 0
for i in range(n):
    if a[i] > 0:
        sv += a[i]
    else:
        k = -a[i]
        if k <= sv:
            sv -= k
        else:
            ans += (k - sv)
            sv = 0
print(ans)
