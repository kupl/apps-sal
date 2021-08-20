(n, k) = map(int, input().split())
cnt = 0
for ab in range(1 - n, n):
    cd = k - ab
    if 1 - n <= cd <= n - 1:
        cnt += (n - abs(ab)) * (n - abs(cd))
print(cnt)
