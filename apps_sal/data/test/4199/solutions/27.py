(n, k) = map(int, input().split())
h = list(map(int, input().split()))
ans = 0
for i in h:
    if k <= i:
        ans += 1
print(ans)
