N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
cnt = [0] * (N + 1)
ans = 0
for i in range(1, N + 1):
    if i - A[i] >= 0:
        ans += cnt[i - A[i]]
    if i + A[i] <= N:
        cnt[i + A[i]] += 1
print(ans)
