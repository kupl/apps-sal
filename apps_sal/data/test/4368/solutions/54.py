(n, k) = map(int, input().split())
lists = []
ans = 0
while True:
    if n < k:
        ans += 1
        break
    (n, b) = divmod(n, k)
    ans += 1
print(ans)
