(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 100
for i in a:
    if k % i == 0:
        ans = min(k // i, ans)
print(ans)
