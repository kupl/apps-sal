(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = x
for i in range(n):
    if a[i] < x:
        ans -= 1
    if a[i] == x:
        ans += 1
print(ans)
