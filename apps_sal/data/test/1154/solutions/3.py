read = lambda: list(map(int, input().split()))
n, h, k = read()
a = list(read())
ans = rem = 0
for i in range(n):
    if rem != 0 and rem + a[i] > h:
        ans += 1
    else:
        a[i] += rem
    ans += a[i] // k
    rem = a[i] % k
if rem != 0:
    ans += 1
print(ans)
    

