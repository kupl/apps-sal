n, k = list(map(int, input().split()))
h = list(map(int, input().split()))
ans = 0
for x in h:
    if x >= k:
        ans += 1
print(ans)
