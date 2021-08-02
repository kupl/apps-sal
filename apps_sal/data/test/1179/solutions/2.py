n, k = map(int, input().split())
IDs = list(map(int, input().split()))

ans = 0
for i in range(1, n + 1):
    if i < k:
        k -= i
    else:
        ans = IDs[k - 1]
        break

print(ans)
