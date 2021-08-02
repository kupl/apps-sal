n = int(input())
l = list(map(int, input().split()))
ans, mod = 0, 0
for i in range(n):
    if(mod > 0):
        a = min(l[i] // 2, mod)
        ans += a
        mod -= a
        l[i] -= 2 * a
    ans += l[i] // 3
    mod += l[i] % 3
print(ans)
