(n, k) = list(map(int, input().split()))
lists = []
ans = 0
while int(n) > 0:
    (n, b) = divmod(n, k)
    ans += 1
print(ans)
