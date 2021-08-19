(n, k) = list(map(int, input().split()))
L = list(map(int, input().split()))
L.sort(reverse=True)
ans = 0
cnt = k
for i in range(n):
    if cnt == k:
        ans += 2 * (L[i] - 1)
        cnt = 1
    else:
        cnt += 1
print(ans)
